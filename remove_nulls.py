import pandas as pd

SOURCE_FILE = "final_converted_out.csv"
OUTPUT_FILENAME = "final_converted_out_dropped.csv"

def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    specs_df = specs_df.dropna(subset=["Misc_Price","Platform_GPU"],axis=0) 
    specs_df.to_csv(OUTPUT_FILENAME, index = False)
main()