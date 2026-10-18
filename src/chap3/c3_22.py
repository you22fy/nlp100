"""
22. カテゴリ名の抽出
"""

import re

from c3_common import load_text


def main():
    text: str = load_text("イギリス")

    # [[Category:名前]] または [[Category:名前|ソートキー]]
    names: list[str] = re.findall(r"^\[\[Category:([^|\]]+)", text, re.MULTILINE)
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
