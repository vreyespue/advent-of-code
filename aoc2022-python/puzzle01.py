import pandas as pd
import numpy as np

# Part #1
df1 = pd.read_csv("../aoc2022-input/input01.txt", header=None, skip_blank_lines=False)
print(df1[0:10])
print(" ")

g = df1.iloc[:, 0].isna()
df2 = df1[~g].groupby(g.cumsum()).apply(sum)
print(df2)
print(" ")

df2.index.name = None
df2_sorted = df2.sort_values(by=0, ascending=False)
df2_top3 = df2_sorted.head(3)
print(df2_top3)
print(" ")

# Part #2
print(df2_top3.sum())
print(" ")
