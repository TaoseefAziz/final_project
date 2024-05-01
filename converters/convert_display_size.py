import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re

SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_display_size.csv"

def convert_display_size(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Display_Size"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['display_diagonal_inches','display_area_cm2','display_screen_body_ratio']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:
        row = filtered_df.iloc[index]
        
        row_data_str = row["Display_Size"].strip().lower()
        row_data_lst = row_data_str.split()
        diagonal_in = row_data_lst[0]

        if "cm2" in row_data_str:
            area_cm2 = row_data_lst[2]
            row["display_area_cm2"]  = area_cm2.strip(" cm2")

        if '%' in row_data_str:
            ratio = row_data_lst[4][2:6]
            row["display_screen_body_ratio"]  = ratio

        row["display_diagonal_inches"] = diagonal_in.strip(" inches")
        
        new_df.loc[len(new_df)] = row

        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df

# def main():
#     specs_df = pd.read_csv(SOURCE_FILE)
#     print(specs_df.shape)
#     out_df = convert_display_size(specs_df)
#     out_df.to_csv(OUTPUT_FILENAME, index = False)

# main()
