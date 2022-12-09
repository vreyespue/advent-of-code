import pandas as pd
import numpy as np
import copy


def compNewTail(H, T):
    if H[0] == T[0]:
        if H[1] > T[1]:
            return (H[0], H[1] - 1)
        elif H[1] < T[1]:
            return (H[0], H[1] + 1)
    elif H[1] == T[1]:
        if H[0] > T[0]:
            return (H[0] - 1, H[1])
        elif H[0] < T[0]:
            return (H[0] + 1, H[1])
    elif H[1] >= T[1] + 2:
        return (H[0], H[1] - 1)
    elif H[1] <= T[1] - 2:
        return (H[0], H[1] + 1)
    elif H[0] >= T[0] + 2:
        return (H[0] - 1, H[1])
    elif H[0] <= T[0] - 2:
        return (H[0] + 1, H[1])

    return T


H = (0, 0)
T = (0, 0)

setPositionsTail = set()

with open(
    "../aoc2022-input/input09.txt",
) as file:
    for line in file:
        currCmd = line.rstrip()
        # print(" ")
        # print(currCmd)

        direction = currCmd[0]
        distance = int(currCmd[2:])

        for i in range(0, distance):

            if direction == "U":
                H = (H[0] + 1, H[1])
            elif direction == "D":
                H = (H[0] - 1, H[1])
            elif direction == "R":
                H = (H[0], H[1] + 1)
            elif direction == "L":
                H = (H[0], H[1] - 1)

            T = compNewTail(H, T)
            setPositionsTail.add(T)

            # print("H: ", H)
            # print("T: ", T)
            # print("setPositionsTail: ", setPositionsTail)

        # if direction == "U":
        #     break

print(" ")
print("H: ", H)
print("T: ", T)
print("len(setPositionsTail): ", len(setPositionsTail))
print(" ")
