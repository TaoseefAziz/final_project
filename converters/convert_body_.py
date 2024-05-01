import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re
from utils import regex
from sklearn import preprocessing

SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_body_.csv"

def convert_body_sim(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Body"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_column_data = {'body_water_resist_ip_rating':''}

    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + list(new_column_data.keys()))

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:
        row = filtered_df.iloc[index]
       
        row_data = row["Body"].strip().lower().replace('\n','')
        row_data_list = row_data.split()
        for entry in row_data_list:
            ip_ratings = []
            if 'ip' in entry:
                ip_ratings = entry.split('/')
                for ip_rating in ip_ratings:
                    rating = ip_rating[2:]

                new_column_data["body_water_resist_ip_rating"] = rating
        
        # print(new_column_data)
        for k, v in new_column_data.items():
            row[k] = v
        new_df.loc[len(new_df)] = row

        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df


def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_body_sim(specs_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()
