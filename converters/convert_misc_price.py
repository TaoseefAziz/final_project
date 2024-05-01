import re

import numpy
import pandas as pd
from utils import converter_templates

about_regex = re.compile(r"About (\d+) ([A-Z]+)")
currency_regex = re.compile(r"(.+) ([0-9.,]+)")

CONVERSIONS = {
    "$": 1,
    "C$": 0.73,
    "£": 1.25,
    "EUR": 1.07,
    "€": 1.07,
    "₹": 0.012,
    "INR": 0.012,
}

EURO_TO_DOLLAR = CONVERSIONS["€"]


def convert_price(df: pd.DataFrame) -> pd.DataFrame:
    def price_converter(price_str: str) -> float | None:
        if not price_str or type(price_str) is float and numpy.isnan(price_str):
            return None

        # print(price_str)

        split = price_str.split("/")

        if len(split) > 1:
            # return the average of the prices if multiple are specified
            return sum(map(price_converter, split)) / len(split)

        price_str = split[0].strip()

        if price_str.startswith("About"):
            match = about_regex.search(price_str)

            amount_str = match.group(1)
            symbol = match.group(2)
        else:
            match = currency_regex.search(price_str)
            symbol = match.group(1)
            amount_str = match.group(2)

        amount = float(amount_str.replace(",", ""))

        return amount * CONVERSIONS[symbol]

    return converter_templates.convert_column(df, "Misc_Price", average_dollar_price=price_converter)
