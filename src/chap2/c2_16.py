"""
16. ランダムに各行を並び替える
"""

import random
from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[2] / 'data' / 'popular-names.txt'

    with open(path) as f:
        lines: list[str] = f.readlines()

    random.shuffle(lines)

    for line in lines:
        print(line, end="")


if __name__ == "__main__":
    main()
