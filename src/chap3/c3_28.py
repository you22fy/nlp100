"""
28. MediaWikiマークアップの除去
"""

import re

from c3_27 import remove_emphasis, remove_internal_links
from c3_common import extract_template, load_text


def remove_markup(value: str) -> str:
    # <ref ... /> と <ref>...</ref> (出典) は中身ごと消す
    value = re.sub(r"<ref[^>]*/>", "", value)
    value = re.sub(r"<ref[^>]*>.*?</ref>", "", value, flags=re.DOTALL)
    # [[ファイル:名前|...]] -> 名前
    value = re.sub(r"\[\[(?:ファイル|File):([^|\]]+)[^\]]*\]\]", r"\1", value)
    # {{仮リンク|表示|en|English}} -> 表示
    value = re.sub(r"\{\{仮リンク\|([^|}]*)\|[^}]*\}\}", r"\1", value)
    # {{lang|en|文字列}} や {{center|文字列}} のように最後の引数が本文のテンプレート -> 文字列
    value = re.sub(r"\{\{[^|{}]*\|(?:[^|{}]*\|)*([^|{}]*)\}\}", r"\1", value)
    # {{0}} や {{en icon}} のように引数のないテンプレート -> 消す
    value = re.sub(r"\{\{[^|{}]*\}\}", "", value)
    # [http://... 表示] -> 表示, [http://...] -> 消す
    value = re.sub(r"\[https?://[^\s\]]+\s+([^\]]+)\]", r"\1", value)
    value = re.sub(r"\[https?://[^\]]+\]", "", value)
    # <br /> は改行の代わりなので空白にし、<references/> など残りの HTML タグは消す
    value = re.sub(r"<br\s*/?>", " ", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("&nbsp;", " ")
    return value.strip()


def clean(value: str) -> str:
    value = remove_emphasis(value)
    value = remove_internal_links(value)
    value = remove_markup(value)
    return value


def main():
    text: str = load_text("イギリス")

    info: dict[str, str] = extract_template(text)
    for key, value in info.items():
        print(f"{key}: {clean(value)}")


if __name__ == "__main__":
    main()
