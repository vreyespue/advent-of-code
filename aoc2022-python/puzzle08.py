import pandas as pd
import numpy as np
import copy


# Part 1
df1 = pd.read_csv(
    "../aoc2022-input/input08.txt",
    header=None,
    index_col=False,
    skip_blank_lines=False,
    sep=" ",
)
df1.rename(columns={0: "A"}, inplace=True)
print(df1)
print(" ")

df1["B"] = df1["A"].str.split("")
print(df1)
print(" ")

df1["C"] = df1.apply(lambda row: list(filter(None, row["B"])), axis=1)
print(df1)
print(" ")

arrays = df1["C"].to_numpy()
grid = np.stack(arrays, axis=0).astype(int)
print(grid)
print(grid.shape)
print(" ")

print(grid[1:3, 1:3])
print(" ")

nrVisibleTrees = 0
for i in range(0, grid.shape[0]):
    for j in range(0, grid.shape[1]):
        # print("i = ", i)
        # print("j = ", j)
        # print("grid[i, j] = ", grid[i, j])
        # print("grid[0:i, j] = ", grid[0:i, j])
        # print("all(grid[0:i, j]>grid[i, j]) = ", all(grid[0:i, j] < grid[i, j]))
        # print(" ")
        if all(grid[:i, j] < grid[i, j]) or (
            all(grid[i + 1 :, j] < grid[i, j])
            or all(grid[i, :j] < grid[i, j])
            or all(grid[i, j + 1 :] < grid[i, j])
        ):
            nrVisibleTrees = nrVisibleTrees + 1

print("Part 1: ", nrVisibleTrees)
print(" ")

scenicScore = np.zeros(shape=grid.shape, dtype=int)
for i in range(1, grid.shape[0]):
    for j in range(1, grid.shape[1]):

        currScoreLeft = 0
        xi = i
        while xi > 0:
            xi = xi - 1
            currScoreLeft = currScoreLeft + 1
            if grid[xi, j] >= grid[i, j]:
                break

        currScoreRight = 0
        xi = i
        while xi < grid.shape[0] - 1:
            xi = xi + 1
            currScoreRight = currScoreRight + 1
            if grid[xi, j] >= grid[i, j]:
                break

        currScoreUp = 0
        xj = j
        while xj > 0:
            xj = xj - 1
            currScoreUp = currScoreUp + 1
            if grid[i, xj] >= grid[i, j]:
                break

        currScoreDown = 0
        xj = j
        while xj < grid.shape[1] - 1:
            xj = xj + 1
            currScoreDown = currScoreDown + 1
            if grid[i, xj] >= grid[i, j]:
                break

        scenicScore[i, j] = currScoreLeft * currScoreRight * currScoreUp * currScoreDown

print(scenicScore[:10, :10])
print(scenicScore.shape)
print(" ")

print("Part 2: ", np.max(scenicScore))
print(" ")
