import pandas as pd
import numpy as np
import copy


# Part 1
currDir = ()
dictDirs = {}

with open(
    "../aoc2022-input/input07.txt",
) as file:
    line = file.readline().rstrip()
    while True:
        currCmd = line.rstrip()
        # print(currCmd)
        if currCmd[2:7] == "cd ..":
            currDir = currDir[:-1]
            line = file.readline().rstrip()
        elif currCmd[2:4] == "cd":
            currDir = currDir + (currCmd[5:],)
            if currDir not in dictDirs:
                dictDirs[currDir] = 0
            line = file.readline().rstrip()
        elif currCmd[2:4] == "ls":
            # while not $ read new line and count size of currDir
            line = file.readline().rstrip()
            if not line:
                break
            while line[0] != "$":
                if line[0] != "d":
                    for i in range(1, len(currDir) + 1):
                        dictDirs[currDir[0:i]] += int(line.split()[0])
                line = file.readline().rstrip()
                if not line:
                    break
        if not line:
            break

print("dictDirs: ", dictDirs)
print(" ")

df1 = pd.DataFrame.from_dict(dictDirs, orient="index")
df1.columns = ["size"]
df1["freeIfDeleted"] = df1["size"] + 21270855
df1 = df1.sort_values(by="size", ascending=False)
print("df1: ", df1[:20])
print(" ")
df1 = df1.loc[df1["size"] < 100000]
print("df1: ", df1)
print(" ")
print("Part 1: ", df1["size"].sum())
