"""
10. 行数のカウント
"""


def main():
    file_path: str = "data/popular-names.txt"

    with open(file_path) as f:
        lines: list[str] = f.readlines()

    print(len(lines))


if __name__ == "__main__":
    main()
