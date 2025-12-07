#!/usr/bin/env python3
import os


input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input_mock.txt")


def parseInput():
    with open(input_file) as f:
        return [x.strip().split() for x in f.readlines()]


def parseInput2():
    with open(input_file) as f:
        return [x[0:-1] for x in f.readlines()]


def part1():
    data = parseInput()
    total = 0

    for colIndex in range(len(data[0])):
        operation = data[-1][colIndex]
        current = int(data[0][colIndex])

        for rowIndex in range(1, len(data) - 1):
            if operation == "*":
                current *= int(data[rowIndex][colIndex])
            else:
                current += int(data[rowIndex][colIndex])

        total += current

    print(total)


def part2():
    data = parseInput2()
    total = 0

    currOperation = data[-1][0]
    currTotal = 1

    for colIndex in range(len(data[0])):
        nums = []

        if not data[-1][colIndex] == ' ':
            currOperation = data[-1][colIndex]
            if currOperation == "+":
                currTotal = 0
            else:
                currTotal = 1

        for rowIndex in range(len(data) - 1):
            if not data[rowIndex][colIndex] == " ":
                nums.append(data[rowIndex][colIndex])

        if len(nums) == 0:
            total += currTotal
            continue

        num = int("".join(nums))

        if currOperation == "+":
            currTotal += num
        else:
            currTotal *= num

    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
