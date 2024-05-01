import pandas as pd

SOURCE_FILE = "specifications.csv"
REMOVED_EMPTY_COLS_FILE = "specs_battery_type_converted.csv"

def convert_battery_type(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Battery_Type"]
    filtered_df = source_dataframe.dropna(subset=["Battery_Type"])
    new_columns = ['Battery_Capacity','Battery_Removability']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)
    for index, row in filtered_df.iterrows():
        battery_type_entry = row['Battery_Type']
        battery_info_lst = battery_type_entry.strip().replace(',','').split()
        if "mAh" not in battery_info_lst:
            continue
        # "mAh" in battery_info_lst
        found_capacity = False
        found_removability = False
        battery_info_lst
        for item in battery_info_lst:
            if item.isnumeric() and not found_capacity:
                row['Battery_Capacity'] = item
                found_capacity = True
            if not found_removability and "non" in item.lower():
                row['Battery_Removability'] = 0
                found_removability = True
            elif not found_removability and "removable" in item.lower():
                found_removability = True
                row['Battery_Removability'] = 1
        if not found_removability:
            row['Battery_Removability'] = 2
        new_df.loc[len(new_df)] = row
    new_df = new_df.drop(source_columns, axis = 1)
    return new_df
# def main():
#     specs_df = pd.read_csv(SOURCE_FILE)
#     print(specs_df.shape)
#     out_df = convert_battery_type(specs_df)
#     out_df.to_csv(REMOVED_EMPTY_COLS_FILE, index = False)
# main()