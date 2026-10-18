"""
第3章で共通して使う関数
"""

import gzip
import json
import re


def load_text(title: str) -> str:
    """jawiki-country.json.gz から title の記事本文を返す"""
    with gzip.open("data/jawiki-country.json.gz", "rt") as f:
        for line in f:
            article: dict = json.loads(line)
            if article["title"] == title:
                return article["text"]
    return ""


def extract_template(text: str) -> dict[str, str]:
    """記事本文から「基礎情報」テンプレートを {フィールド名: 値} の辞書にして返す"""
    # {{基礎情報 ... }} のブロック (閉じる }} は行頭にある)
    template: str = re.search(
        r"^\{\{基礎情報.*?^\}\}$", text, re.MULTILINE | re.DOTALL
    ).group()

    # "|フィールド名 = 値" を取り出す。値は次の "|" で始まる行、または末尾の "}}" まで (複数行あり)
    fields: list[tuple[str, str]] = re.findall(
        r"^\|([^=\n]+?)\s*=\s*(.*?)(?=\n\||\n\}\})",
        template,
        re.MULTILINE | re.DOTALL,
    )
    return dict(fields)
