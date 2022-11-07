import pandas as pd
import numpy as np

# Part #1
df1 = pd.read_csv("../aoc2021_input/input01.txt", header=None)
print(df1)
df1_diff = df1.diff()
print(df1_diff)
df1_diff_pos = df1_diff[df1_diff > 0].dropna()
print(df1_diff_pos)
print("\nResult part #1: " + str(df1_diff_pos.shape[0]) + "\n")

# Part #2
df2 = df1.rolling(3).sum()
print(df2)
df2_diff = df2.diff()
print(df2_diff)
df2_diff_pos = df2_diff[df2_diff > 0].dropna()
print(df2_diff_pos)
print("\nResult part #2: " + str(df2_diff_pos.shape[0]) + "\n")
