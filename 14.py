from pathlib import Path
import pandas as pd


def amount_before_2022(excel_path: str | Path):
    df = pd.read_excel(excel_path)
    df2 = pd.concat([df["amount"], df["registration_date"]], axis=1)
    records = df2.loc[df2["registration_date"] < "2022-01-01"]
    return records["amount"].sum()


def amount_per_rating(excel_path: str | Path):
    df = pd.read_excel(excel_path)
    df2 = pd.concat([df["amount"], df["rating"]], axis=1)
    records = df2.groupby(["rating"]).sum()
    return records
