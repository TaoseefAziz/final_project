import pandas as pd
from utils import converter_templates


def convert_jack(df: pd.DataFrame) -> pd.DataFrame:
    def jack_bool(val: str):
        if val == "Yes" or val == "No":
            return int(val == "Yes")

        return None

    return converter_templates.convert_column(df, "Sound_3.5mm jack ", has_jack=jack_bool)


def convert_loudspeaker(df: pd.DataFrame) -> pd.DataFrame:
    def loudspeaker_bool(val: str):
        if val.startswith("Yes") or val.startswith("No"):
            return int(val.startswith("Yes"))

        return None

    def stereo_bool(val: str):
        if val.startswith("Yes") or val.startswith("No"):
            return int("stereo speakers" in val)

        return None

    def dual_bool(val: str):
        if val.startswith("Yes") or val.startswith("No"):
            return int("dual speakers" in val)

        return None

    return converter_templates.convert_column(df, "Sound_Loudspeaker", has_loudspeaker=loudspeaker_bool,
                                              has_stereo=stereo_bool, has_dual=dual_bool)
