import pandas as pd
import numpy as np

# Part #1
df1 = pd.read_csv("../aoc2021_input/input01.txt", header=None)
print(df1)
df1_diff = df1.diff()
print(df1_diff)
df1_diff_pos = df1_diff[df1_diff > 0].dropna()
print(df1_diff_pos)
print("Result part #1: " + str(df1_diff_pos.shape[0]))

# Part #2
