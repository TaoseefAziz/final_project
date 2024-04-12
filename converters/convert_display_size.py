import pandas as pd
from utils import regex, converter_templates


def convert_display_size(df: pd.DataFrame) -> pd.DataFrame:
    size_extractor = regex.extractor_generator(r"(\d+\.\d+) inches")
    area_extractor = regex.extractor_generator(r"(\d+\.\d+) cm2")
    ratio_extractor = regex.extractor_generator(r"\(~(\d+\.\d+)% screen-to-body ratio\)")

    return converter_templates.convert_column(df, "Display_Size", screen_size=size_extractor,
                                              area=area_extractor, ratio=ratio_extractor)
