"""
18. 各行の1列目の文字列の出現頻度を求め、出現頻度の高い順に並べる
"""


def main():
    file_path: str = "data/popular-names.txt"

    with open(file_path) as f:
        lines: list[str] = f.readlines()

    counts: dict[str, int] = {}
    for line in lines:
        name: str = line.split("\t")[0]
        counts[name] = counts.get(name, 0) + 1

    # 出現頻度の降順、同数なら名前の昇順。
    for name, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{count} {name}")


if __name__ == "__main__":
    main()
