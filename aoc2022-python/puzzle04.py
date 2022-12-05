import pandas as pd
import numpy as np

# Part #1
df1 = pd.read_csv(
    "../aoc2022-input/input04.txt",
    header=None,
    index_col=False,
    skip_blank_lines=False,
    sep="-|,",
)
print(df1)
print(" ")
df1.rename(columns={0: "a1", 1: "a2", 2: "b1", 3: "b2"}, inplace=True)
print(df1)
print(" ")

df1["aR"] = df1.apply(lambda row: set(np.arange(row["a1"], row["a2"] + 1)), axis=1)
df1["bR"] = df1.apply(lambda row: set(np.arange(row["b1"], row["b2"] + 1)), axis=1)
print(df1)
print(" ")

df1["isSub"] = df1.apply(
    lambda row: ((row["aR"].issubset(row["bR"])) | (row["bR"].issubset(row["aR"]))),
    axis=1,
)
print(df1)
print(" ")

print("Part #1: ", df1["isSub"].sum())

df1["hasIntersect"] = df1.apply(
    lambda row: len(row["aR"].intersection(row["bR"])) != 0, axis=1
)
print(df1[0:50])
print(" ")

print("Part #2: ", df1["hasIntersect"].sum())
