#!/usr/bin/env python3
import os


input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input_mock.txt")


def parseInput():
    with open(input_file) as f:
        return [list(x.rstrip()) for x in f.readlines()]


def checkSurrounding(i, j, rowLength, grid):
    count = 0

    if i > 0 and grid[i-1][j] == "@":
        count += 1

    if i < len(grid) - 1 and grid[i+1][j] == "@":
        count += 1

    if j > 0 and grid[i][j-1] == "@":
        count += 1

    if j < rowLength - 1 and grid[i][j+1] == "@":
        count += 1

    if i > 0 and j > 0 and grid[i-1][j-1] == "@":
        count += 1

    if i > 0 and j < rowLength - 1 and grid[i-1][j+1] == "@":
        count += 1

    if i < rowLength - 1 and j > 0 and grid[i+1][j-1] == "@":
        count += 1

    if i < rowLength - 1 and j < rowLength - 1 and grid[i+1][j+1] == "@":
        count += 1

    return count


def part1():
    grid = parseInput()
    total = 0
    for (i, row) in enumerate(grid):
        for (j, cell) in enumerate(row):
            if cell == ".":
                continue
            count = checkSurrounding(i, j, len(row), grid)
            if count < 4:
                total += 1

    print(total)


def part2():
    grid = parseInput()
    total = 0

    while True:
        currTotal = total
        for (i, row) in enumerate(grid):
            for (j, cell) in enumerate(row):
                if cell == ".":
                    continue
                count = checkSurrounding(i, j, len(row), grid)

                if count < 4:
                    currTotal += 1
                    grid[i][j] = "."

        if currTotal == total:
            break
        total = currTotal

    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
