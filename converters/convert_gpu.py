import pandas as pd
import sklearn.preprocessing as preprocessing
from utils import converter_templates


def convert_gpu(df: pd.DataFrame) -> pd.DataFrame:
    encoder = preprocessing.OneHotEncoder(sparse_output=False)

    def standardize_gpu(gpu_str: str) -> str | None:
        if not gpu_str or type(gpu_str) is float:
            return None

        if "/" in gpu_str:
            # if there are multiple GPUs, just disregard this entry
            return None

        return gpu_str.replace(" ", "")

    standardized = converter_templates.convert_column(df, "Platform_GPU", standardized_gpu=standardize_gpu)

    encoded = pd.DataFrame(encoder.fit_transform(standardized[["standardized_gpu"]]))

    encoded.rename(lambda name: f"gpu_{name}", inplace=True, axis=1)

    concatted = pd.concat([standardized, encoded], axis=1)

    return concatted
