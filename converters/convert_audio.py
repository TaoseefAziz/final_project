import pandas as pd
from utils import converter_templates


def convert_jack(df: pd.DataFrame) -> pd.DataFrame:
    def jack_bool(val: str):
        if val == "Yes" or val == "No":
            return val == "Yes"

        return None

    return converter_templates.convert_column(df, "Sound_3.5mm jack ", has_jack=jack_bool)
