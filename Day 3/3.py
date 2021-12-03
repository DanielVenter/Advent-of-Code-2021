
import numpy as np

with open("input.txt", "r") as f:
    lines = np.array([list(line.replace("\n", "")) for line in f.readlines()])

    lines_t = lines.transpose()
    gamma = []
    epsilon = []
    for line in lines_t:
        line = [int(i) for i in line]
        ones = np.count_nonzero(line)
        zeros = len(line) - ones

        if ones > zeros:
            gamma.append("1")
            epsilon.append("0")
        elif zeros > ones:
            gamma.append("0")
            epsilon.append("1")

    gamma_int, epsilon_int = int("".join(gamma), 2), int("".join(epsilon), 2)

    print(gamma_int, epsilon_int)
    print(gamma_int*epsilon_int)


