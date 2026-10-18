"""
24. ファイル参照の抽出
"""

import re

from c3_common import load_text


def main():
    text: str = load_text("イギリス")

    # [[ファイル:名前|...]] や [[File:名前]] の名前部分
    files: list[str] = re.findall(r"\[\[(?:ファイル|File):([^|\]]+)", text)
    for file in files:
        print(file)


if __name__ == "__main__":
    main()
