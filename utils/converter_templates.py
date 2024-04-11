import pandas as pd
from utils import regex


def replace_column(df: pd.DataFrame, column: str, **new_cols_and_regexes: str) -> pd.DataFrame:
    extracted_column = df[column]

    # using the dictionary as the intermediate data structure lol
    for new_col, new_col_regex in new_cols_and_regexes.items():
        new_cols_and_regexes[new_col] = extracted_column.map(regex.extractor_generator(new_col_regex))

    return df.assign(**new_cols_and_regexes).drop(columns=[column]).dropna(subset=list(new_cols_and_regexes))
