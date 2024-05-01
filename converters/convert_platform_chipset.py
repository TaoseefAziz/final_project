import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re


SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_platform_chipset.csv"

def convert_platform_chipset(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Platform_Chipset"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['platform_chipset_manufacturer','platform_chipset_details','platform_chipset_node']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:


        row = filtered_df.iloc[index]
        
        row_data_str = row["Platform_Chipset"].strip().lower()
        row_data_lst = row_data_str.split()

        if len(row_data_lst) < 2:
            index += 1
            continue

        chip_manufacturer = ""
        chip_details = []
        chip_node = "0"
        chip_manufacturer_found = False
        for entry in row_data_lst:
            if entry.isalpha() and not chip_manufacturer_found:
                chip_manufacturer = entry
                chip_manufacturer_found = True
            if not entry.isalpha():
                chip_details.append(entry)
            if '(' in entry:
                for c in entry:
                    if c.isnumeric():
                        chip_node += c
                if 0 < int(chip_node) < 60:
                    row['platform_chipset_node'] = int(chip_node)

        row['platform_chipset_manufacturer'] = chip_manufacturer
        for detail in chip_details:
            if len(detail) > 2:
                row['platform_chipset_details'] = detail
                break
        
        new_df.loc[len(new_df)] = row

        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df


def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_platform_chipset(specs_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()
