from typing import LiteralString


def main():
    s: str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    s: LiteralString = s.replace(".", "").replace(",", "")
    r: list[int] = [len(si) for si in s.split()]
    print(r)


if __name__ == "__main__":
    main()
