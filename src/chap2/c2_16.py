"""
16. ランダムに各行を並び替える
"""

import random


def main():
    file_path: str = "data/popular-names.txt"

    with open(file_path) as f:
        lines: list[str] = f.readlines()

    random.shuffle(lines)

    for line in lines:
        print(line, end="")


if __name__ == "__main__":
    main()
