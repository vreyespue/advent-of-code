import pandas as pd
import numpy as np


def scoreForChoice(choice):
    match choice:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3


def scoreForGame(choiceA, choiceB):
    if (
        (choiceA == "A" and choiceB == "X")
        or (choiceA == "B" and choiceB == "Y")
        or (choiceA == "C" and choiceB == "Z")
    ):
        return 3
    elif (
        (choiceA == "A" and choiceB == "Y")
        or (choiceA == "B" and choiceB == "Z")
        or (choiceA == "C" and choiceB == "X")
    ):
        return 6
    else:
        return 0


def scoreForOption(choiceP1, choiceP2):
    match choiceP2:
        case "X":  # lose
            match choiceP1:
                case "A":
                    return 0 + scoreForChoice("Z")
                case "B":
                    return 0 + scoreForChoice("X")
                case "C":
                    return 0 + scoreForChoice("Y")
        case "Y":  # draw
            match choiceP1:
                case "A":
                    return 3 + scoreForChoice("X")
                case "B":
                    return 3 + scoreForChoice("Y")
                case "C":
                    return 3 + scoreForChoice("Z")
        case "Z":  # win
            match choiceP1:
                case "A":
                    return 6 + scoreForChoice("Y")
                case "B":
                    return 6 + scoreForChoice("Z")
                case "C":
                    return 6 + scoreForChoice("X")


# Part #1
df1 = pd.read_csv(
    "../aoc2022-input/input02.txt",
    header=None,
    index_col=False,
    skip_blank_lines=False,
    sep=" ",
)
print(df1)
print(" ")
df1.rename(columns={0: "P1", 1: "P2"}, inplace=True)
print(df1)
print(" ")

df1["scoreChoice"] = df1.apply(lambda row: scoreForChoice(row["P2"]), axis=1)
print(df1)
print(" ")

df1["scoreGame"] = df1.apply(lambda row: scoreForGame(row["P1"], row["P2"]), axis=1)
print(df1)
print(" ")

df1["scoreAllV1"] = df1["scoreChoice"] + df1["scoreGame"]
print(df1)
print(" ")

print("Part #1: ", df1["scoreAllV1"].sum())
print(" ")

# Part #2
df1["scoreOption"] = df1.apply(lambda row: scoreForOption(row["P1"], row["P2"]), axis=1)
print(df1)
print(" ")

print("Part #2: ", df1["scoreOption"].sum())
print(" ")
