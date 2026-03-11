import pandas as pd
import numpy as np

def clean_wb_wide(
    df: pd.DataFrame,
    drop_top_rows: int = 0,
    drop_last_rows: int = 5,
    drop_left_cols: int = 2,
    missing_tokens = ('..',),
    year_regex: str = r'(\d{4})',
):
    """
    Cleans World Bank-style wide indicator CSVs where the table has:
      - metadata rows/cols to drop
      - 'Series Code' and 'Series Name' rows after transpose
      - year columns like '1960 [YR1960]'
    Returns:
      data_clean: DataFrame with columns ['Year', <series codes...>]
      series_lookup: DataFrame with ['Series Code', 'Series Name']
    """

    # 1) trim and standardize missing values
    df = (
        df.iloc[drop_top_rows: len(df)-drop_last_rows if drop_last_rows else None, drop_left_cols:]
          .replace(list(missing_tokens), np.nan)
    )

    # 2) series lookup (keep once)
    series_lookup = (
        df[['Series Code', 'Series Name']]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    # 3) transpose with year on columns
    out = df.T
    out.columns = out.loc['Series Code']
    out.columns.name = None
    out = out.drop(index=['Series Name', 'Series Code'])

    # 4) clean year index
    out.index = out.index.astype(str).str.extract(year_regex)[0].astype(int)

    # 5) numeric + make Year a column
    out = out.astype(float)
    out.index.name = 'Year'
    out = out.reset_index()

    return out, series_lookup