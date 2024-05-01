import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re

from utils import regex

SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_body_weight.csv"

def convert_body_weight(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Body_Weight"]
    filtered_df = source_dataframe.dropna(subset=source_columns)

    new_columns = ['Body_Weight_g']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)
    
    for index, row in filtered_df.iterrows():
        rex = r"(\d+\.*\d*)\s*g"
        extractor = regex.extractor_generator(rex)
        match = extractor(str(row["Body_Weight"]))
        if match:
            row["Body_Weight_g"] = match
            new_df.loc[len(new_df)] = row
        # else:
            # print("No weight found")

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting Body_Weight")

    return new_df


# def main():
#     specs_df = pd.read_csv(SOURCE_FILE)
#     print(specs_df.shape)
#     out_df = convert_body_weight(specs_df)
#     out_df.to_csv(OUTPUT_FILENAME, index = False)

# main()
