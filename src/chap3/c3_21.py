"""
21. カテゴリ名を含む行を抽出
"""

import re

from c3_common import load_text


def main():
    text: str = load_text("イギリス")

    lines: list[str] = re.findall(r"^\[\[Category:.*$", text, re.MULTILINE)
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
