"""
26. 強調マークアップの除去
"""

import re

from c3_common import extract_template, load_text


def remove_emphasis(value: str) -> str:
    # ''弱い強調'' / '''強調''' / '''''強い強調''''' のクォートを消す
    return re.sub(r"'{2,5}", "", value)


def main():
    text: str = load_text("イギリス")

    info: dict[str, str] = extract_template(text)
    for key, value in info.items():
        print(f"{key}: {remove_emphasis(value)}")


if __name__ == "__main__":
    main()
