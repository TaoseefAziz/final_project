import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re


SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_display_type.csv"

def convert_display_type(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Display_Type"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['display_tech','display_refresh']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:
        row = filtered_df.iloc[index]
        
        row_data_str = row["Display_Type"].strip().lower()
        row_data_lst = row_data_str.split(',')
        
        row["display_tech"] = row_data_lst[0]
        if "hz" in row_data_str:
            for entry in row_data_lst:
                if "hz" in entry:
                    row["display_refresh"] = int(entry[:-2])
        else:
            row["display_refresh"] = 60
        new_df.loc[len(new_df)] = row

        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df


def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_display_type(specs_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()
