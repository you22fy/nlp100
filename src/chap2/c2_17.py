"""
17. １列目の文字列の異なり
"""


from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[2] / 'data' / 'popular-names.txt'

    with open(path) as f:
        lines: list[str] = f.readlines()

    names: set[str] = set()
    for line in lines:
        names.add(line.split("\t")[0])

    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    main()
