#!/usr/bin/env python3
import os


input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input_mock.txt")


def parseInput():
    with open(input_file) as f:
        return [tuple([int(y) for y in x.rstrip().split(",")]) for x in f.readlines()]


def part1():
    coords = parseInput()
    maxArea = 0

    for i, p1 in enumerate(coords):
        for j in range(i+1, len(coords)):
            p2 = coords[j]

            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            maxArea = max(area, maxArea)

    print(maxArea)


def main():
    part1()


if __name__ == "__main__":
    main()
