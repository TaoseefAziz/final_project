import pandas as pd
from utils import regex, converter_templates


def convert_display_size(df: pd.DataFrame) -> pd.DataFrame:
    screen_size_regex = regex.extractor_generator(r"(\d+\.\d+) inches")
    area_regex = regex.extractor_generator(r"(\d+\.\d+) cm2")
    ratio_regex = regex.extractor_generator(r"\(~(\d+\.\d+)% screen-to-body ratio\)")

    return converter_templates.replace_column(df, "Display_Size", screen_size=screen_size_regex,
                                              area=area_regex, ratio=ratio_regex)
