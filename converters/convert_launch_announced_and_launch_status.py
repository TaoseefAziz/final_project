import pandas as pd

SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_launch_announced_and_launch_status.csv"

def convert_launch_announced_and_launch_status(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Launch_Announced", 'Launch_Status']
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['Launch_year',"IsAvailable"]
    
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)
    
    for index, row in filtered_df.iterrows():
        launch_announced_entry = row['Launch_Announced']
        launch_announced_lst = launch_announced_entry.strip().replace('.',',').split(',')

        launch_status_entry = row['Launch_Status']
        launch_status_lst = launch_status_entry.strip().replace(',','').replace('.','').split()

        announced_year = 1970
        if launch_announced_lst[0].isnumeric():
            announced_year = int(launch_announced_lst[0])
        status_year = 1970
        if "Released" in launch_status_lst:
            status_year = int(launch_status_lst[2])
        max_year = max(announced_year, status_year)
        row['Launch_year'] = max_year

        if "Available" in launch_status_lst[0]:
            row['IsAvailable'] = 1
        else:
            row['IsAvailable'] = 1

        new_df.loc[len(new_df)] = row

    new_df = new_df.drop(source_columns, axis = 1)
    return new_df

def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_launch_announced_and_launch_status(specs_df)


    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()