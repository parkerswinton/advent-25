#!/usr/bin/env python3

import os

input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input.txt")


def part1():
    curr = 50
    total = 0
    with open(input_file) as f:
        for line in f:
            l = line.rstrip()
            direction = -1 if l[0] == "L" else 1
            amount = int(l[1:])

            curr += direction * amount
            curr %= 100

            if curr == 0:
                total += 1

    print(total)


def part2():
    curr = 50
    total = 0
    with open(input_file) as f:
        for line in f:
            l = line.rstrip()
            direction = -1 if l[0] == 'L' else 1
            amount = int(l[1:])
            prev = curr

            if direction > 0:
                total += (curr + amount) // 100
            else:
                if prev == 0:
                    if amount >= 100:
                        total += abs((curr - amount) // 100) - 1
                else:
                    total += abs((curr - amount) // 100)

                if (curr - amount) % 100 == 0:
                    total += 1

            curr = (curr + (direction * amount)) % 100

    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
