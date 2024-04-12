import pandas as pd

SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_body_dimensions.csv"

def convert_body_dimensions(source_dataframe: pd.DataFrame) -> pd.DataFrame:
    source_columns = ["Body_Dimensions"]
    print(f"before converting  using columns = {source_columns} size = {source_dataframe.shape}")
    filtered_df = source_dataframe.dropna(subset=source_columns)

    new_columns = ['Body_length_mm',"Body_width_mm","Body_depth_mm"]
    
    new_df = pd.DataFrame(columns=filtered_df.columns.tolist() + new_columns)
    
    for index, row in filtered_df.iterrows():
        body_dimensions_entry = row['Body_Dimensions']
        body_dimensions_lst = body_dimensions_entry.strip().split('(')
        body_dimensions_mm_only = body_dimensions_lst[0]

        if len(body_dimensions_mm_only.split("x")) == 3:
            each_dimension_lst = body_dimensions_mm_only.split("x")
            length_mm = float(each_dimension_lst[0].strip())
            width_mm = float(each_dimension_lst[1].strip())
            depth_mm = -1

            depth = each_dimension_lst[2]
            depth_parsed = depth.split("mm")[0].strip()
            if "-" in depth_parsed:
                depth_lo_hi = depth_parsed.split('-')
                depth_lo = float(depth_lo_hi[0].strip())
                depth_hi = float(depth_lo_hi[1].strip())
                depth_mm = round(( depth_lo + depth_hi ) / 2, 1)
            else:
                depth_mm = float(depth_parsed)

            row["Body_length_mm"] = length_mm
            row["Body_width_mm"] = width_mm
            row["Body_depth_mm"] = depth_mm

            new_df.loc[len(new_df)] = row

    new_df = new_df.drop(source_columns, axis = 1)
    print(f"after converting = {new_df.shape}")

    return new_df

def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_body_dimensions(specs_df)


    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()