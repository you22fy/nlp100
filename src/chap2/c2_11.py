"""
11. 先頭からN行を出力
"""


from itertools import islice
from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[2] / 'data' / 'popular-names.txt'
    n: int = 10

    with open(path) as f:
        for line in islice(f, n):
            print(line, end="")


if __name__ == "__main__":
    main()
