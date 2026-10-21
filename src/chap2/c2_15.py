"""
15. ファイルをN分割する
"""


from itertools import islice
from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[2] / 'data' / 'popular-names.txt'
    n: int = 10
    prefix: str = "data/split_py_"

    with open(path) as f:
        line_count = sum(1 for _ in f)
        size: int = (line_count + n - 1) // n
        f.seek(0)

        for i in range(n):
            if i * size >= line_count:
                break
            out_path: str = f"{prefix}{i:02d}"
            with open(out_path, "w") as out:
                out.writelines(islice(f, size))
            print(out_path)


if __name__ == "__main__":
    main()
