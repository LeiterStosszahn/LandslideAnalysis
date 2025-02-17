import pandas as pd

def StoD(data: pd.Series) -> pd.Series:
    df = pd.DataFrame()
    df[["Degrees", "Minutes", "Seconds"]] = data.str.extract(r"(\d+)°\s*(\d+)\'\s*(\d+)\"").astype(float)
    df["Decimal"] = df["Degrees"] + (df["Minutes"] / 60) + (df["Seconds"] / 3600)

    return df["Decimal"]