import pandas as pd
import typing


def convert_column(df: pd.DataFrame, column: str, drop_original: bool = True, drop_new_nas: bool = True,
                   **new_cols_and_funcs: typing.Callable[[str], typing.Any]) -> pd.DataFrame:
    """
    Convert a column into one or more columns, each with a value extracted from the values of the original column

    :param df: the DataFrame
    :param column: the column to convert
    :param drop_original: whether to drop the original column
    :param drop_new_nas: whether to drop rows that have a value of N/A in any of the new columns
    :param new_cols_and_funcs: keyword arguments, one for each new column. For each column, the column name will be the
        argument's name, and the values will be extracted from the original column using the function specified by the
        argument's value.
    :return: a copy of the DataFrame after the operation
    """

    extracted_column = df[column]

    # using the dictionary as the intermediate data structure lol
    for new_col, new_col_func in new_cols_and_funcs.items():
        new_cols_and_funcs[new_col] = extracted_column.map(new_col_func)

    new_df = df.assign(**new_cols_and_funcs)

    if drop_original:
        new_df.drop(columns=[column], inplace=True)

    if drop_new_nas:
        new_df.dropna(subset=list(new_cols_and_funcs), inplace=True)

    return new_df
