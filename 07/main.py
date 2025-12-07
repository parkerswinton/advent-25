#!/usr/bin/env python3
import os
# from pprint import pprint

input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input_mock.txt")


def parseInput():
    with open(input_file) as f:
        return [list(x.rstrip()) for x in f.readlines()]


def part1():
    grid = parseInput()

    startIndex = grid[0].index("S")
    grid[1][startIndex] = "|"

    splits = 0

    for rowIndex in range(1, len(grid) - 1):
        for colIndex in range(len(grid[rowIndex])):
            curr = grid[rowIndex][colIndex]
            if curr == "|":
                if grid[rowIndex + 1][colIndex] == "^":
                    splits += 1
                    grid[rowIndex + 1][colIndex - 1] = "|"
                    grid[rowIndex + 1][colIndex + 1] = "|"
                else:
                    grid[rowIndex + 1][colIndex] = "|"
    print(splits)


def main():
    part1()


if __name__ == "__main__":
    main()
