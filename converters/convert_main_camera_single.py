import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re


SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_main_camera_single.csv"

def convert_main_camera_single(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Main Camera_Single"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['main_camera_single_mp']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:
        row = filtered_df.iloc[index]
        
        row_data_str = row["Main Camera_Single"].strip().lower()
        row_data_lst = row_data_str.split()

        idx_mp = 0
        cam_mp_value = 0
        for idx in range(len(row_data_lst)):
            entry = row_data_lst[idx]
            if 'mp' in entry:
                idx_mp = idx
                cam_mp_value = row_data_lst[idx-1]
                row["main_camera_single_mp"] = cam_mp_value

        new_df.loc[len(new_df)] = row
        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df


def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_main_camera_single(specs_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()
