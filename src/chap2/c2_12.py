"""
12. 末尾のN行を出力
"""


from collections import deque
from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[2] / 'data' / 'popular-names.txt'
    n: int = 10

    with open(path) as f:
        lines = deque(f, maxlen=n)

    for line in lines:
        print(line, end="")


if __name__ == "__main__":
    main()
