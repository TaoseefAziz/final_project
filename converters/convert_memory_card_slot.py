import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re


SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_platform_memcard_slot.csv"

def convert_memory_card_slot(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Memory_Card slot"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['memory_card_slot']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:
        row = filtered_df.iloc[index]
        
        row_data_str = row["Memory_Card slot"].strip().lower()
        row_data_lst = row_data_str.split()

        row["memory_card_slot"] = row_data_lst[0]
        
        new_df.loc[len(new_df)] = row

        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df


def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_memory_card_slot(specs_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()
