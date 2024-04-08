import pandas as pd
import re
import typing


def convert_display_size(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset="Display_Size")

    display_size = df["Display_Size"]

    screen_size_regex = r"(\d+\.\d+) inches"
    area_regex = r"(\d+\.\d+) cm2"
    ratio_regex = r"\(~(\d+\.\d+)% screen-to-body ratio\)"

    def extractor_generator(regex: str) -> typing.Callable[[str], str]:
        def extractor(val: str) -> str | None:
            match = re.search(regex, str(val))

            if not match:
                return match

            return match.group(1)

        return extractor

    screen_size = display_size.map(extractor_generator(screen_size_regex))
    area = display_size.map(extractor_generator(area_regex))
    ratio = display_size.map(extractor_generator(ratio_regex))

    converted = df.assign(screen_size=screen_size, screen_area=area, screen_ratio=ratio).drop(
        columns=["Display_Size"]).dropna(subset=["screen_size", "screen_area", "screen_ratio"])

    return converted
