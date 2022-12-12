import pandas as pd
import numpy as np
import re


def getStrength(df, signal):
    value = df1.loc[df1["cycle_cum"] <= signal].tail(1)["val_cum"].values[0]
    strength = value * signal
    return strength


df1 = pd.read_csv(
    "../aoc2022-input/input10.txt",
    header=None,
    index_col=False,
    skip_blank_lines=True,
    sep=" ",
)
df1.rename(columns={0: "op", 1: "val_float"}, inplace=True)
df1["cycle_diff"] = df1.apply(lambda x: 2 if x["op"] == "addx" else 1, axis=1)
df1["val_int"] = df1["val_float"].fillna(0).astype(int)
df1["cycle_cum"] = df1["cycle_diff"].cumsum() + 1
df1["val_cum"] = df1["val_int"].cumsum() + 1
print(df1)
print(" ")

df2 = df1.loc[df1["cycle_cum"] < 20].tail(1)
print(df2[:20])
print(" ")

total_strength = (
    getStrength(df1, 20)
    + getStrength(df1, 60)
    + getStrength(df1, 100)
    + getStrength(df1, 140)
    + getStrength(df1, 180)
    + getStrength(df1, 220)
)
print("Part #1: ", total_strength)
print(" ")

df3 = pd.Series(range(1, 241)).to_frame()
df3.rename(columns={0: "cycle"}, inplace=True)
df3 = df3.join(
    df1[["cycle_cum", "val_cum"]].set_index("cycle_cum"), on="cycle", how="left"
)
df3["val_cum"] = df3["val_cum"].fillna(method="bfill").astype(int)
df3["val_cum"][0] = 1
df3["val_cum"][1] = 1
df3["cycle_col"] = ((df3["cycle"] - 1) % 40) + 1
df3["cycle_row"] = ((df3["cycle"] - 1) / 40) + 1
df3["cycle_row"] = df3["cycle_row"].astype(int)
df3["symbol"] = df3.apply(
    lambda x: "#" if abs(x["cycle_col"] - x["val_cum"]) <= 1 else ".", axis=1
)
print(df3)
print(" ")

strRes = df3["symbol"].to_string(index=False).strip().replace("\n", "")
strRes2 = re.findall(".{1,40}", strRes)
print(*strRes2, sep="\n")
print(" ")
