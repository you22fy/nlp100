"""
15. ファイルをN分割する
"""


def main():
    file_path: str = "data/popular-names.txt"
    n: int = 10
    prefix: str = "data/split_py_"

    with open(file_path) as f:
        lines: list[str] = f.readlines()

    # 1ファイルあたりの行数 (切り上げ)
    size: int = (len(lines) + n - 1) // n

    for i in range(n):
        chunk: list[str] = lines[i * size : (i + 1) * size]
        if not chunk:
            break
        out_path: str = f"{prefix}{i:02d}"
        with open(out_path, "w") as f:
            f.writelines(chunk)
        print(out_path)


if __name__ == "__main__":
    main()
