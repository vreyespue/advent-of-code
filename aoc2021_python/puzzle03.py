import pandas as pd
import numpy as np

# Part #1
df1 = pd.read_csv("../aoc2021_input/input03.txt", header=None, dtype=str)
print(df1)
df2 = df1[0].apply(lambda x: pd.Series(list(x)))
print(df2)

gamma = np.zeros(12, dtype=int)
epsilon = np.zeros(12, dtype=int)
for idx in range(df2.shape[1]):
    gamma[idx] = df2[idx].mode()
    epsilon[idx] = df2[idx].value_counts().idxmin()
print(gamma)
print(epsilon)

gammaInt = (gamma.dot(1) << np.arange(gamma.shape[-1] - 1, -1, -1)).sum()
epsilonInt = (epsilon.dot(1) << np.arange(epsilon.shape[-1] - 1, -1, -1)).sum()

print("\nResult part #1: " + str(gammaInt * epsilonInt) + "\n")
