import os
import glob
import pandas as pd
from typing import List

def read_excel_files(path: str) -> List[pd.DataFrame]:
    """
        Function to read all excel files in a folder.
        :param path: str, required: Part of the files names to be search.
        :return: list
    """
    files = glob.glob(os.path.join(path, "*.xlsx"))

    if not files:
        raise ValueError("No Excel files found in the specified folder")

    return [pd.read_excel(file) for file in files]