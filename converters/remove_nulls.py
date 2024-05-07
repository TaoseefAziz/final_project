import pandas as pd

SOURCE_FILE = "converted_all_taoseef_extended_dropped.csv"
OUTPUT_FILENAME = "converted_all_taoseef_extended_dropped.csv"

def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    specs_df = specs_df.dropna(subset=["Misc_Price","Platform_GPU"],axis=0) 
    specs_df.to_csv(OUTPUT_FILENAME, index = False)
main()