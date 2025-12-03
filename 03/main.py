#!/usr/bin/env python3
import os


input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")


def parseInput():
    with open(input_file) as f:
        return [x.rstrip() for x in f.readlines()]


def part1():
    banks = parseInput()
    total = 0
    for b in banks:
        maxFirst, maxFirstIndex = 0, 0
        for (i, n) in enumerate(b[0:len(b) - 1]):
            if int(n) > maxFirst:
                maxFirst = int(n)
                maxFirstIndex = i

        maxLast = 0
        for i in range(maxFirstIndex + 1, len(b)):
            if int(b[i]) > maxLast:
                maxLast = int(b[i])

        total += maxFirst * 10 + maxLast

    print(total)


def part2():
    banks = parseInput()
    rev = [b[::-1] for b in banks]

    total = 0

    for b in rev:
        ans = []
        prevMaxIndex = len(b)
        for i in range(12):
            maxValue = 0
            for j in range(11-i, prevMaxIndex):
                if int(b[j]) >= maxValue:
                    maxValue = int(b[j])
                    prevMaxIndex = j

            ans.append(maxValue)

        for (i, a) in enumerate(ans):
            total += 10**(11 - i) * a

    print(total)


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
