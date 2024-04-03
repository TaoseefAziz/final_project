import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

req_interval = 2

def get_manufacturers():
    url = "https://www.gsmarena.com/makers.php3"

    time.sleep(req_interval)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    manufacturer_urls = {}
    all_urls = soup.find_all('a')
    i = 0
    for link in all_urls:
        href = link.get('href')
        if 19 < i < 122 + 19 + 1: # 19 garbage urls, 122 manufacturers
            if href != None and 'php' in href:
                phone_manufacturer = href.split('-')[0]
                manufacturer_urls[phone_manufacturer] = f"https://www.gsmarena.com/{href}"
        i += 1

    return manufacturer_urls

def get_popular_sorted_pages(manufacturer_urls):

    popular_page_urls = {}
    num_manufacturers = 2

    i = 0
    for manufacturer, url in manufacturer_urls.items():
        if i < num_manufacturers:

            time.sleep(req_interval)
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            sortby_popularity_url = soup.find("i",class_="head-icon icon-popularity").parent.get('href')
            popular_page_urls[manufacturer] = f"https://www.gsmarena.com/{sortby_popularity_url}"
            print(f"https://www.gsmarena.com/{sortby_popularity_url}")

        i += 1

    return popular_page_urls

def get_popular_devices_all_manufacturers(popular_page_urls):
    devices_df = pd.DataFrame(columns=['manufacturer', 'device', 'url'])
    manufacturers = 2
    devices_per_page = 2
    start_devices = 23 # garbage urls in this many 'a' tags

    i = 0
    for manufacturer, popular_devices_url in popular_page_urls.items():
        if i < manufacturers:

            time.sleep(req_interval)
            response = requests.get(popular_devices_url)

            soup = BeautifulSoup(response.text, 'html.parser')
            popular_devices_lst = []
            all_devices = soup.findAll("a")

            j = 0
            for device in all_devices:
                if start_devices < j < start_devices + devices_per_page + 1:
                    device_url = device.get("href")
                    device_name = device_url.split('-')[0]
                    full_url = f"https://www.gsmarena.com/{device_url}"
                    devices_df.loc[len(devices_df)] = (manufacturer, device_name, full_url)
                j += 1
        i += 1

    return devices_df

def get_specifications_for_device(device_url, specifications_df):
    time.sleep(req_interval)
    response = requests.get(device_url, headers = {'User-agent': 'bot'})

    soup = BeautifulSoup(response.text, 'html.parser')
    
    if int(response.status_code) == 429:
        print("Denied for too many requests")
        print(response.headers["Retry-After"])

    feature_tables = soup.findAll("table")

    for feature_table in feature_tables:
        feature_class = feature_table.find('th').text
        feature_names = feature_table.findAll(class_='ttl')
        feature_values = feature_table.findAll(class_='nfo')
        for i in range(len(feature_names)):
            key = feature_class +"_" + feature_names[i].text
            value = feature_values[i].text
            specifications_df[key] = value

    return feature_tables

if __name__ == "__main__": 
    # get urls for all the manufacturers on the site
    manufacturer_urls = get_manufacturers()

    # get urls for the popular devices for each manufacturer
    popular_page_urls = get_popular_sorted_pages(manufacturer_urls)

    devices_df = get_popular_devices_all_manufacturers(popular_page_urls)

    for index, row in devices_df.iterrows():
        url = row['url']
        get_specifications_for_device(url,devices_df)
    
    devices_df.to_csv('output_specs.csv')

