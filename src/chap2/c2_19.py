"""
19. 3列目の数値の降順に各行を並び替える
"""


def main():
    file_path: str = "data/popular-names.txt"

    with open(file_path) as f:
        lines: list[str] = f.readlines()

    # sort は安定なので、3列目が同じ行は元の順序を保つ。
    lines.sort(key=lambda line: int(line.split("\t")[2]), reverse=True)

    for line in lines:
        print(line, end="")


if __name__ == "__main__":
    main()
