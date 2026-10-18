"""
27. 内部リンクの除去
"""

import re

from c3_26 import remove_emphasis
from c3_common import extract_template, load_text


def remove_internal_links(value: str) -> str:
    # [[記事名]] -> 記事名, [[記事名|表示]] -> 表示, [[記事名#節|表示]] -> 表示
    # ファイルへのリンク ([[ファイル:...]]) は内部リンクではないので対象外
    return re.sub(r"\[\[(?!ファイル:|File:)(?:[^|\]]*?\|)?([^\]]*?)\]\]", r"\1", value)


def main():
    text: str = load_text("イギリス")

    info: dict[str, str] = extract_template(text)
    for key, value in info.items():
        value = remove_emphasis(value)
        value = remove_internal_links(value)
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
