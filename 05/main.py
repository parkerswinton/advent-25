#!/usr/bin/env python3
import os


input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input_mock.txt")


def parseInput():
    with open(input_file) as f:
        lines = [x.rstrip() for x in f.readlines()]
        i = lines.index('')
        ranges = [tuple([int(y) for y in x.split("-")]) for x in lines[:i]]
        values = [int(x) for x in lines[i+1:]]
        return ranges, values


def part1():
    ranges, values = parseInput()

    count = 0
    for v in values:
        for r in ranges:
            lower, upper = r
            if v >= lower and v <= upper:
                count += 1
                break

    print(count)


def part2():
    ranges, _ = parseInput()
    ranges.sort(key=lambda x: x[0])
    stack = []

    for r in ranges:
        if not stack or stack[-1][1] < r[0]:
            stack.append(r)
            continue

        if stack[-1][1] < r[1]:
            top = stack.pop()
            stack.append((top[0], r[1]))

    total = 0
    for v in stack:
        total += v[1] - v[0] + 1

    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
