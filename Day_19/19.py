import numpy as np
import math
from copy import deepcopy
from itertools import combinations


def rotations():
    """Generate all possible rotation functions"""
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(np.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = np.cross(vi, vj)

                def transform(x):
                    return np.matmul(x, np.array([vi, vj, vk]))

                yield transform


def fit(scanners, hashes, i, j, v):
    """Find the correct rotation/translation to make the jth scanner map fit the ith"""
    s1, s2 = scanners[i], scanners[j]
    for rot in rotations():
        s2t = rot(s2)
        for p in hashes[i][v]:
            for q in hashes[j][v]:
                diff = s1[p, :] - s2t[q, :]
                if len(set(map(tuple, s2t + diff)) & set(map(tuple, s1))) >= 12:
                    return diff, set(map(tuple, s2t + diff)), rot


def map_hash(coords):
    """
    Generate a hashset of sorted absolute coordinate differences
    between pairs of points
    """
    s = {
        tuple(sorted(map(abs, coords[i, :] - coords[j, :]))): (i, j)
        for i, j in combinations(range(len(coords)), 2)
    }
    return s


def match(scanners, hashes):
    """Figure out which pairs of scanner aps have sufficient overlap"""
    for i, j in combinations(range(len(hashes)), 2):
        if len(m:=set(hashes[i]) & set(hashes[j])) >= math.comb(12, 2):
            yield i, j, next(iter(m))


def solve(scanners):
    """Given a list of scanner maps, return list of positions and set of beacons"""
    scanners = deepcopy(scanners)
    positions = {0: (0, 0, 0)}
    hashes = list(map(map_hash, scanners))
    beacons = set(map(tuple, scanners[0]))
    while len(positions) < len(scanners):
        for i, j, v in match(scanners, hashes):
            if i not in positions and j not in positions:
                continue
            elif i in positions and j in positions:
                continue
            elif j in positions:
                i, j = j, i
            positions[j], new_beacons, rot = fit(scanners, hashes, i, j, v)
            scanners[j] = rot(scanners[j]) + positions[j]
            beacons.update(new_beacons) 
    return [positions[i] for i in range(len(scanners))], beacons


with open("input.txt", "r") as data:
    data = data.read()

scanners = data.split("\n\n")
scanners = [x.split("---\n")[-1].split("\n") for x in scanners]
scanners = [np.array([list(map(int, y.split(","))) for y in x]) for x in scanners]

positions, beacons = solve(scanners)
print(len(beacons))
print(max(np.abs(x - y).sum() for x, y in combinations(positions, 2)))