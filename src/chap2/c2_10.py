"""
10. 行数のカウント
"""


from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[2] / 'data' / 'popular-names.txt'

    with open(path) as f:
        lines: list[str] = f.readlines()

    print(len(lines))


if __name__ == "__main__":
    main()
