#!/usr/bin/env python3
import os
import math

input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input_mock.txt")


def calculateDistance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)


def calculateDistances(coords):
    distances = []

    for i, p1 in enumerate(coords):
        for j in range(i+1, len(coords)):
            p2 = coords[j]
            distances.append([p1, p2, calculateDistance(p1, p2)])

    distances.sort(key=lambda x: x[2])
    return distances


def parseInput():
    with open(input_file) as f:
        return [tuple([int(y) for y in x.rstrip().split(",")]) for x in f.readlines()]


def part1():
    coords = parseInput()
    distances = calculateDistances(coords)

    connections = 10

    circuits = []

    for distance in distances:
        p1, p2, _ = distance

        p1Index, p2Index = None, None
        for i, c in enumerate(circuits):
            if p1 in c:
                p1Index = i
            if p2 in c:
                p2Index = i

        if p1Index == None:
            if p2Index == None:
                circuits.append([p1, p2])
            else:
                circuits[p2Index].append(p1)
        else:
            if p2Index == None:
                circuits[p1Index].append(p2)
            elif not p1Index == p2Index:
                maxI = max(p1Index, p2Index)
                minI = min(p1Index, p2Index)

                c1 = circuits.pop(maxI)
                c2 = circuits.pop(minI)

                circuits.append(c1 + c2)

        connections -= 1
        if not connections > 0:
            break

    circuits.sort(key=len, reverse=True)
    ans = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    print(ans)


def part2():
    coords = parseInput()
    distances = calculateDistances(coords)

    circuits = []

    for distance in distances:
        p1, p2, _ = distance

        p1Index, p2Index = None, None
        for i, c in enumerate(circuits):
            if p1 in c:
                p1Index = i
            if p2 in c:
                p2Index = i

        if p1Index == None:
            if p2Index == None:
                circuits.append([p1, p2])
            else:
                circuits[p2Index].append(p1)
        else:
            if p2Index == None:
                circuits[p1Index].append(p2)
            elif not p1Index == p2Index:
                maxI = max(p1Index, p2Index)
                minI = min(p1Index, p2Index)

                c1 = circuits.pop(maxI)
                c2 = circuits.pop(minI)

                circuits.append(c1 + c2)

        if len(circuits) == 1 and len(circuits[0]) == len(coords):
            print(p1[0] * p2[0])
            break


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
