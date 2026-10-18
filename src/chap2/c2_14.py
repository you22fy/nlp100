"""
14. 1列目を出力
"""


def main():
    file_path: str = "data/popular-names.txt"
    n: int = 10

    with open(file_path) as f:
        lines: list[str] = f.readlines()

    for line in lines[:n]:
        print(line.split("\t")[0])


if __name__ == "__main__":
    main()
