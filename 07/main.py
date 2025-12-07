#!/usr/bin/env python3
import os

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


def part2():
    grid = parseInput()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ".":
                grid[i][j] = 0

    startIndex = grid[0].index("S")
    grid[1][startIndex] = 1

    for rowIndex in range(1, len(grid) - 1):
        for colIndex in range(len(grid[rowIndex])):
            curr = grid[rowIndex][colIndex]
            if not curr == 0 and not curr == "^":
                if grid[rowIndex + 1][colIndex] == "^":
                    grid[rowIndex + 1][colIndex - 1] += curr
                    grid[rowIndex + 1][colIndex + 1] += curr
                else:
                    grid[rowIndex + 1][colIndex] += curr

    timelines = 0

    for num in grid[-1]:
        timelines += num

    print(timelines)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
