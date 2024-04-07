import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

REQ_INTERVAL = 0
RESTRICT_NUM_MAN = 122
GARBAGE_MANF_URLS = 19
GARBAGE_DEV_URLS = 23
TOTAL_MANUFACTURERS = 122
NUM_DEVICES_PER_MANF = 15
ROOT_URL = "https://www.gsmarena.com/makers.php3"

MANUFACTURERS_URLS_FILE = "man_urls.csv"
POP_URLS_FILE = "pop_urls.csv"
DEVICE_URLS_FILE = "device_urls.csv"
SPECIFICATIONS_FILE = "sepcifications.csv"

def get_gsmarena_manufacturers(root_url, existing_df):
    new_df = pd.DataFrame(columns=['manufacturer', 'url'])

    response = requests.get(root_url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'html.parser')
    all_urls = soup.find_all('a')

    i = 0
    for link in all_urls:
        href = link.get('href')
        if GARBAGE_MANF_URLS < i < TOTAL_MANUFACTURERS + GARBAGE_MANF_URLS + 1 and \
        href != None and 'php' in href:
            manufacturer = href.split('-')[0]

            # Check to see if this is already in the dataframe
            if not ( existing_df['manufacturer'].eq(manufacturer)).any():
                full_url = f"https://www.gsmarena.com/{href}"
                new_df.loc[len(new_df)] = (manufacturer, full_url)
        i += 1

    return new_df

def get_pop_pages(man_urls_df, old_pop_df):
    new_df = pd.DataFrame(columns=['manufacturer', 'url'])

    i = 0
    for index in man_urls_df.index:
        manufacturer = man_urls_df['manufacturer'][index]
        url = man_urls_df['url'][index]
        if i < RESTRICT_NUM_MAN and not ( old_pop_df['manufacturer'].eq(manufacturer)).any():
            
            time.sleep(REQ_INTERVAL)
            response = requests.get(url)
            assert response.status_code == 200

            soup = BeautifulSoup(response.text, 'html.parser')
            sortby_popularity_url = soup.find("i",class_="head-icon icon-popularity").parent.get('href')
            full_url = f"https://www.gsmarena.com/{sortby_popularity_url}"
            print(f"storing: {manufacturer} {full_url}")
            new_df.loc[len(new_df)] = (manufacturer, full_url)
        i += 1
    return new_df

def get_popular_devices_all_manufacturers(popular_urls_df, old_devices_df):
    new_df = pd.DataFrame(columns=['manufacturer', 'device', 'url'])

    manufacturer_idx = 0
    
    for index in popular_urls_df.index:
        manufacturer = popular_urls_df['manufacturer'][index]
        url = popular_urls_df['url'][index]

        if manufacturer_idx < RESTRICT_NUM_MAN:
            time.sleep(REQ_INTERVAL)
            response = requests.get(url)
            assert response.status_code == 200

            soup = BeautifulSoup(response.text, 'html.parser')
            all_devices = soup.findAll("a")

            device_idx = 0
            for device in all_devices:
                if GARBAGE_DEV_URLS < device_idx < GARBAGE_DEV_URLS + NUM_DEVICES_PER_MANF + 1:
                    device_url = device.get("href")
                    device_name = device_url.split('-')[0]
                    full_url = f"https://www.gsmarena.com/{device_url}"
                    new_row = (manufacturer, device_name, full_url)
                    new_df.loc[len(new_df)] = new_row
                device_idx += 1
        manufacturer_idx += 1

    return new_df

def get_specifications_for_device(manufacturer, device, device_url):
    specifications_dict = {}
    specifications_dict['manufacturer'] = manufacturer
    specifications_dict['device'] = device

    time.sleep(REQ_INTERVAL)
    response = requests.get(device_url, headers = {'User-agent': 'bot'})

    while int(response.status_code) != 200:
        print("Request unsuccessful")
        if (response.status_code == 429):
            print("Too many requests")
            print(response.headers["Retry-After"])
        input("Waiting for RETURN to be pressed to continue")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    feature_tables = soup.findAll("table")

    for feature_table in feature_tables:
        feature_class_header = feature_table.find('th')
        if (feature_class_header != None):
            feature_class = feature_class_header.text
            feature_names = feature_table.findAll(class_='ttl')
            feature_values = feature_table.findAll(class_='nfo')
            for i in range(len(feature_names)):
                key = feature_class +"_" + feature_names[i].text
                value = feature_values[i].text
                specifications_dict[key] = value
                # print(f"writing: {key} --> {value}")

    return specifications_dict

if __name__ == "__main__": 
    # man_urls_old_df = pd.read_csv(MANUFACTURERS_URLS_FILE)
    # man_urls_new_df = get_gsmarena_manufacturers(ROOT_URL,man_urls_old_df)
    # man_urls_updated_df = pd.concat([man_urls_old_df, man_urls_new_df])
    # man_urls_updated_df.to_csv(MANUFACTURERS_URLS_FILE,index=False)

    # pop_urls_old_df = pd.read_csv(POP_URLS_FILE)  
    # pop_urls_new_df = get_pop_pages(man_urls_updated_df, pop_urls_old_df)
    # pop_urls_updated_df = pd.concat([pop_urls_old_df, pop_urls_new_df])
    # pop_urls_updated_df.to_csv(POP_URLS_FILE,index=False)

    # pop_urls_df = pd.read_csv(POP_URLS_FILE)
    # devices_old_df = pd.read_csv(POP_URLS_FILE)  
    # devices_new_df = get_popular_devices_all_manufacturers(pop_urls_df, devices_old_df)
    # devices_new_df.to_csv(DEVICE_URLS_FILE,index=False)

    devices_new_df = pd.read_csv(DEVICE_URLS_FILE)
    all_columns=["manufacturer","device","Network_Technology","Network_2G bands","Network_GPRS",
    "Network_EDGE","Launch_Announced","Launch_Status","Body_Dimensions","Body_Weight","Body_SIM","Body_","Display_Type","Display_Size",
    "Display_Resolution","Platform_OS","Platform_Chipset","Platform_CPU","Memory_Card slot","Memory_Internal","Main Camera_Single",
    "Main Camera_Video","Selfie camera_Single","Selfie camera_Video","Sound_Loudspeaker ","Sound_3.5mm jack ","Comms_WLAN","Comms_Bluetooth",
    "Comms_Positioning","Comms_NFC","Comms_Radio","Comms_USB","Features_Sensors","Battery_Type","Battery_Talk time","Misc_Colors","Misc_Price",
    "Network_3G bands","Network_4G bands","Network_","Network_Speed","Platform_GPU","Main Camera_Features","Memory_","Misc_Models","Body_Build",
    "Main Camera_Triple","Selfie camera_Features"]

    start = 1491
    for index, row in devices_new_df.iterrows():
        if index > start:
            specifications_df =  pd.DataFrame(columns=all_columns)
            specs_dict = get_specifications_for_device(row['manufacturer'],row['device'],row['url'])
            specifications_df.loc[0] = specs_dict
            specifications_df.to_csv(SPECIFICATIONS_FILE, mode = "a",index=False, header = False)
