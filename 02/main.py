#!/usr/bin/env python3
import os


input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")


def parseInput():
    with open(input_file) as f:
        return [[int(n) for n in x.split("-")]
                for x in f.readline().rstrip().split(",")]


def part1():
    ranges = parseInput()
    total = 0
    for r in ranges:
        lower, upper = r[0], r[1]
        for i in range(lower, upper + 1):
            num = str(i)
            if len(num) % 2 == 0 and num[:len(num)//2] == num[len(num)//2:]:
                total += i
    print(total)


def part2():
    ranges = parseInput()
    total = 0

    for r in ranges:
        lower, upper = r[0], r[1]
        for i in range(lower, upper + 1):
            num = str(i)

            for j in range(len(num)//2):
                sub = num[0:j+1]

                count = num.count(sub)
                if len(sub) * count == len(num):
                    total += i
                    break
    print(total)


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
