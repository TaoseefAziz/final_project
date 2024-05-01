import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re


SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_platform_memory_internal.csv"

def convert_memory_internal(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Memory_Internal"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['memory_internal_storage','memory_ram']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:
        row = filtered_df.iloc[index]
        
        row_data_str = row["Memory_Internal"].strip().lower()
        row_data_lst = row_data_str.split()
        ram_indices = []
        ram_values = [0]
        storage_values = [0]

        if len(row_data_lst) < 3:
            index += 1
            continue

        for entry_idx in range(len(row_data_lst)):
            entry = row_data_lst[entry_idx]
            if 'ram' in entry:
                ram_indices.append(entry_idx)
        
        for idx in ram_indices:
            ram_entry = row_data_lst[idx-1]
            if 'gb' in ram_entry:
                ram_values.append(float(ram_entry.strip(",").strip(";").strip().strip('gb')))
            elif 'mb' in ram_entry:
                ram_values.append(float(ram_entry.strip(",").strip(";").strip().strip('mb'))/1000)
            
            storage_entry = row_data_lst[idx-2]
            if 'gb' in storage_entry:
                storage_values.append(float(storage_entry.strip(",").strip(";").strip().strip('gb')))
            elif 'mb' in storage_entry:
                storage_values.append(float(storage_entry.strip(",").strip(";").strip().strip('mb'))/1000)
        if len(ram_values) > 0:
            row["memory_internal_storage"] = max(storage_values)
        if len(storage_values) > 0:
            row["memory_ram"] = max(ram_values)

        new_df.loc[len(new_df)] = row

        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df


def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_memory_internal(specs_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()
