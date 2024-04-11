import pandas as pd
import re
import typing

SOURCE_FILE = "sepcifications.csv"
REMOVED_EMPTY_COLS_FILE = "specs_removed_empty_battery_type.csv"

def convert_battery_type(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    filtered_df = source_dataframe.dropna(subset=["Battery_Type"])
    new_df = pd.DataFrame(columns=filtered_df.columns)
    for index, row in filtered_df.iterrows():
        battery_type_entry = row['Battery_Type']
        battery_info_lst = battery_type_entry.strip().replace(',','').split()
        if "mAh" not in battery_info_lst:
            continue
        # "mAh" in battery_info_lst
        found_capacity = False
        battery_info_lst
        for item in battery_info_lst:
            if item.isnumeric() and not found_capacity:
                row['Battery_Capacity'] = item
                found_capacity = True
            if "non" in item.lower():
                row['Battery_Removability'] = 0
            elif "removable" in item.lower():
                row['Battery_Removability'] = 1
        new_df.loc[len(new_df)] = row

    print(type(row['Battery_Type']))

    new_df.to_csv(REMOVED_EMPTY_COLS_FILE, index = False)
    return new_df
