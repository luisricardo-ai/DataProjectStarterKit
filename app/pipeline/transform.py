import pandas as pd
from typing import List

def concat_dataframes(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframe_list)