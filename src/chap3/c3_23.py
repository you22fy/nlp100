"""
23. セクション構造
"""

import re

from c3_common import load_text


def main():
    text: str = load_text("イギリス")

    # "== 名前 ==" の = の数 - 1 がレベル
    sections: list[tuple[str, str]] = re.findall(r"^(=+)\s*(.+?)\s*\1\s*$", text, re.MULTILINE)
    for marks, name in sections:
        level: int = len(marks) - 1
        print(f"{name}\t{level}")


if __name__ == "__main__":
    main()
