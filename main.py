#!/usr/bin/env python3
import sys
import os
import subprocess

default_text = """#!/usr/bin/env python3
import os


input_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "input_mock.txt")

def main():
    print("DEFAULT")


if __name__ == \"__main__\":
    main()
"""


def generate(day):
    if os.path.exists(day):
        sys.exit(f"Error: Folder '{day}' already exists.")

    os.mkdir(day)

    with open(os.path.join(day, "main.py"), "w") as f:
        f.write(default_text)


def run(day):
    file_path = os.path.join(day, "main.py")
    if not os.path.isfile(file_path):
        sys.exit(f"Error: Folder '{day}' does not exist.")

    subprocess.run(["python3", file_path])


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <mode> <day_number>")
        print("Modes: generate (-g), run (-r)")
        sys.exit()

    mode = sys.argv[1].lower()
    day = sys.argv[2]

    match mode:
        case "generate" | "gen" | "g" | "-g":
            generate(day)
        case "run" | "r" | "-r":
            run(day)
        case _:
            sys.exit("Error: Unknown mode.")


if __name__ == "__main__":
    main()
