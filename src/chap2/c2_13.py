"""
13. タブをスペースに置換
"""


from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[2] / 'data' / 'popular-names.txt'
    n: int = 10

    with open(path) as f:
        lines: list[str] = f.readlines()

    for line in lines[:n]:
        print(line.replace("\t", " "), end="")


if __name__ == "__main__":
    main()
