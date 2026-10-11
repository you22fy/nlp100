from typing import LiteralString


def main():
    s: str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    n: set[int] = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    s: LiteralString = s.replace(".", "").replace(",", "")
    d: dict = {}
    for idx, si in enumerate(s.split()):
        c: int = 1 if idx + 1 in n else 2
        d[si[:c]] = idx + 1

    for k, v in d.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
