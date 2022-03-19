import pandas as pd
import numpy as np

# Part #1
df1 = pd.read_csv("../aoc2021_input/input02.txt", header=None, sep=" ")
print(df1)

df1Forward = df1[df1[0] == "forward"]
sumForward = df1Forward[1].sum()
df1Down = df1[df1[0] == "down"]
sumDown = df1Down[1].sum()
df1Up = df1[df1[0] == "up"]
sumUp = df1Up[1].sum()

print("\nResult part #1: " + str(sumForward * (sumDown - sumUp)) + "\n")
