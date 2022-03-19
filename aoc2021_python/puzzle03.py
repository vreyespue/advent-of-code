import pandas as pd
import numpy as np

# Part #1
df1 = pd.read_csv("../aoc2021_input/input03.txt", header=None, dtype=str)
print(df1)
df2 = df1[0].apply(lambda x: pd.Series(list(x)).astype(int))
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


# Part #2

oxygen = df2
for idx in range(oxygen.shape[1]):
    if oxygen.shape[0] > 1:
        if oxygen[idx].sum() >= (oxygen[idx].size / 2):
            oxygen = oxygen[oxygen[idx] == 1]
        else:
            oxygen = oxygen[oxygen[idx] == 0]
    print("oxygen.shape = " + str(oxygen.shape))

print("\noxygen = ")
print(oxygen)
oxygenNp = np.array(oxygen)
oxygenInt = (oxygenNp.dot(1) << np.arange(oxygenNp.shape[-1] - 1, -1, -1)).sum()
print(oxygenInt)
print("")

co2 = df2
for idx in range(co2.shape[1]):
    if co2.shape[0] > 1:
        if co2[idx].sum() >= (co2[idx].size / 2):
            co2 = co2[co2[idx] == 0]
        else:
            co2 = co2[co2[idx] == 1]
    print("co2.shape = " + str(co2.shape))

print("\nco2 = ")
print(co2)
co2Np = np.array(co2)
co2Int = (co2Np.dot(1) << np.arange(co2Np.shape[-1] - 1, -1, -1)).sum()
print(co2Int)
print("")

print("\nResult part #1: " + str(oxygenInt * co2Int) + "\n")
