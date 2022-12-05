import pandas as pd
import numpy as np
import copy


def popN(list, n):
    return [list.pop() for _ in range(n)]


def popN2(list, n):
    return reversed([list.pop() for _ in range(n)])


stacks = [
    [],
    ["F", "D", "B", "Z", "T", "J", "R", "N"],
    ["R", "S", "N", "J", "H"],
    ["C", "R", "N", "J", "G", "Z", "F", "Q"],
    ["F", "V", "N", "G", "R", "T", "Q"],
    ["L", "T", "Q", "F"],
    ["Q", "C", "W", "Z", "B", "R", "G", "N"],
    ["F", "C", "L", "S", "N", "H", "M"],
    ["D", "N", "Q", "M", "T", "J"],
    ["P", "G", "S"],
]

stacks2 = copy.deepcopy(stacks)

df1 = pd.read_csv(
    "../aoc2022-input/input05.txt",
    header=None,
    index_col=False,
    skip_blank_lines=True,
    sep=" ",
    skiprows=10,
)
print(df1)
print(" ")

# Part #1
print(stacks)
for row in df1.itertuples():
    # print(row)
    stacks[int(row[6])] += popN(stacks[int(row[4])], int(row[2]))
    # print(stacks)
print(stacks)
for stack in stacks[1:]:
    print(stack[-1], end="")
print(" ")
print(" ")

# Part #2
print(stacks2)
for row in df1.itertuples():
    # print(row)
    stacks2[int(row[6])] += popN2(stacks2[int(row[4])], int(row[2]))
    # print(stacks2)
print(stacks2)
for stack2 in stacks2[1:]:
    print(stack2[-1], end="")
