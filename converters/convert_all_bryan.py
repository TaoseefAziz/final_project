from . import convert_audio, convert_gpu, convert_display_size, convert_misc_price
import pandas as pd


def convert_all_bryan(df: pd.DataFrame) -> pd.DataFrame:
    df = convert_audio.convert_jack(df)
    df = convert_audio.convert_loudspeaker(df)
    df = convert_gpu.convert_gpu(df)
    df = convert_misc_price.convert_price(df)
    df = convert_display_size.convert_display_size(df)

    return df
