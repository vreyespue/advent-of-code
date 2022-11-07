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

# Part #2
aim = 0
depth = 0
horiz_pos = 0
df1 = df1.reset_index()
for index, row in df1.iterrows():
    if row[0] == "down":
        aim += row[1]
    elif row[0] == "up":
        aim -= row[1]
    elif row[0] == "forward":
        horiz_pos += row[1]
        depth += aim * row[1]

print("\naim = " + str(aim))
print("depth = " + str(depth))
print("horiz_pos = " + str(horiz_pos))
print("\nResult part #2: " + str(depth * horiz_pos) + "\n")
