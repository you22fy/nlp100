"""
29. 国旗画像のURLを取得する
"""

import requests

from c3_common import extract_template, load_text


def main():
    text: str = load_text("イギリス")
    info: dict[str, str] = extract_template(text)
    file_name: str = info["国旗画像"]

    # MediaWiki API の imageinfo でファイル名を URL に変換する
    response = requests.get(
        "https://ja.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "titles": f"File:{file_name}",
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json",
        },
        headers={"User-Agent": "nlp100-exercise/0.1"},
    )
    pages: dict = response.json()["query"]["pages"]
    for page in pages.values():
        print(page["imageinfo"][0]["url"])


if __name__ == "__main__":
    main()
