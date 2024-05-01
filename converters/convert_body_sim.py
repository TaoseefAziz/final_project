import re
import typing
import sys
import os
sys.path.insert(1, os.getcwd())
import pandas as pd
import re
from utils import regex
from sklearn import preprocessing

SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_body_sim.csv"

def convert_body_sim(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Body_SIM"]
    filtered_df = source_dataframe.dropna(subset=source_columns)
    new_columns = ['num_slots_sim','has_mini_sim','has_nano_sim','has_micro_sim','has_e_sim','stand-by_sim','hybrid_sim']
    num_slots_sim = {'no':0,'single':1,'dual':2,'and':2,',':2,'triple':3}
    has_x_sim = ['mini','nano','micro','esim']
    sim_properties = ['stand-by_sim','hybrid_sim']
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)

    iterate_row_start = 0
    iterate_row_end = len(filtered_df)

    index = iterate_row_start

    while iterate_row_start <= index < iterate_row_end:
        row = filtered_df.iloc[index]
        new_column_entries = {'num_slots_sim':0,'hybrid_sim':0,'has_mini_sim':0,\
            'has_nano_sim':0,'has_micro_sim':0,'has_e_sim':0,'standby_sim':0}
        row_data = row["Body_SIM"].strip().lower()
        variant0 = row_data.split('or')[0]
        
        for key, val in num_slots_sim.items():
            if key in variant0:
                new_column_entries['num_slots_sim'] = val

        for simtype in has_x_sim:
            if simtype in variant0:
                new_column_entries[f'has_{simtype}_sim'] = 1
                # print(f"{variant0} has simtype-->{f'{simtype}'}")
        for column_heading in sim_properties:
            sim_property = column_heading.split('_')[0]
            if sim_property in variant0:
                new_column_entries[column_heading] = 1
            else:
                new_column_entries[column_heading] = 0

        # print(f"{variant0}")
        # for k, v in new_column_entries.items():
        #     print(f"  {k} {v}")
        for k, v in new_column_entries.items():
            # print(f"k{k} v{v}")
            row[k] = v
        new_df.loc[len(new_df)] = row

        index += 1

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"Lost: {source_dataframe.shape[0]-new_df.shape[0]} rows when converting body_sim")

    return new_df


# def main():
#     specs_df = pd.read_csv(SOURCE_FILE)
#     print(specs_df.shape)
#     out_df = convert_body_sim(specs_df)
#     out_df.to_csv(OUTPUT_FILENAME, index = False)

# main()
