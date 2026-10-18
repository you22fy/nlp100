"""
25. テンプレートの抽出
"""

from c3_common import extract_template, load_text


def main():
    text: str = load_text("イギリス")

    info: dict[str, str] = extract_template(text)
    for key, value in info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
