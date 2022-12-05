import pandas as pd
import numpy as np


# Part #1
df1 = pd.read_csv(
    "../aoc2022-input/input03.txt",
    header=None,
    index_col=False,
    skip_blank_lines=False,
    sep=" ",
)
print(df1)
print(" ")

# firstpart, secondpart = string[:len(string)/2], string[len(string)/2:]
# df1[["A", "B"]] = df1[0][: len(df1[0]) / 2], df1[0][len(df1[0]) / 2 :]
df1["A"] = df1.apply(lambda row: row[0][: int(len(row[0]) / 2)], axis=1)
df1["B"] = df1.apply(lambda row: row[0][int(len(row[0]) / 2) :], axis=1)
df1["C"] = df1.apply(lambda row: list(set(row["A"]) & set(row["B"]))[0], axis=1)
df1["D"] = df1.apply(
    lambda row: (ord(row["C"]) - 38) if (row["C"] < "a") else (ord(row["C"]) - 96),
    axis=1,
)
print(df1)
print(" ")
print("Part #1: ", df1["D"].sum())
print(" ")

x = np.arange(1, 101)
print(x)
print(" ")
y = np.repeat(x, 3, axis=0)
print(y)
print(" ")

df1["G"] = pd.Series(y).apply(lambda row: int(row))
print(df1)
print(" ")

df2 = pd.DataFrame()
df2["g"] = df1[0].groupby(df1["G"]).apply(list)
print(df2)
print(" ")

df2["badge"] = df2.apply(
    lambda row: list(set(row["g"][0]) & set(row["g"][1]) & set(row["g"][2]))[0], axis=1
)
print(df2)
print(" ")

df2["res"] = df2.apply(
    lambda row: (ord(row["badge"]) - 38)
    if (row["badge"] < "a")
    else (ord(row["badge"]) - 96),
    axis=1,
)
print(df2)
print(" ")

print("Part #2: ", df2["res"].sum())
print(" ")
