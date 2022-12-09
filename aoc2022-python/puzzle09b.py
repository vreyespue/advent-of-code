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

    elif H[0] >= T[0] + 2 and H[1] >= T[1] + 2:
        return (H[0] - 1, H[1] - 1)
    elif H[0] >= T[0] + 2 and H[1] <= T[1] - 2:
        return (H[0] - 1, H[1] + 1)
    elif H[0] <= T[0] - 2 and H[1] >= T[1] + 2:
        return (H[0] + 1, H[1] - 1)
    elif H[0] <= T[0] - 2 and H[1] <= T[1] - 2:
        return (H[0] + 1, H[1] + 1)

    elif H[0] >= T[0] + 2:
        return (H[0] - 1, H[1])
    elif H[0] <= T[0] - 2:
        return (H[0] + 1, H[1])
    elif H[1] >= T[1] + 2:
        return (H[0], H[1] - 1)
    elif H[1] <= T[1] - 2:
        return (H[0], H[1] + 1)

    return T


rope = [(0, 0)] * 10

setPositionsTail = set()

print(rope)
print(" ")

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
                rope[0] = (rope[0][0] + 1, rope[0][1])
            elif direction == "D":
                rope[0] = (rope[0][0] - 1, rope[0][1])
            elif direction == "R":
                rope[0] = (rope[0][0], rope[0][1] + 1)
            elif direction == "L":
                rope[0] = (rope[0][0], rope[0][1] - 1)

            for j in range(1, len(rope)):
                rope[j] = compNewTail(rope[j - 1], rope[j])

            setPositionsTail.add(rope[len(rope) - 1])

            # print("H: ", H)
            # print("T: ", T)
            # print("setPositionsTail: ", setPositionsTail)

        # if direction == "U":
        #     break

print(" ")
print("snake: ", rope)
print("len(setPositionsTail): ", len(setPositionsTail))
print(" ")
