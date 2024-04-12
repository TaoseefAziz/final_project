import pandas as pd
from utils import regex
import typing


def replace_column(df: pd.DataFrame, column: str,
                   **new_cols_and_funcs: typing.Callable[[str], typing.Any]) -> pd.DataFrame:
    """
    Replace column with one or more columns, each with a value extracted from the values of the original column

    :param df: the DataFrame
    :param column: the column to replace
    :param new_cols_and_funcs: keyword arguments, one for each new column. For each column, the column name
        will be the argument's name, and the values will be extracted from the original column using the
        function specified by the argument's value.
    :return: a copy of the DataFrame after the operation
    """

    extracted_column = df[column]

    # using the dictionary as the intermediate data structure lol
    for new_col, new_col_func in new_cols_and_funcs.items():
        new_cols_and_funcs[new_col] = extracted_column.map(new_col_func)

    return df.assign(**new_cols_and_funcs).drop(columns=[column]).dropna(subset=list(new_cols_and_funcs))
