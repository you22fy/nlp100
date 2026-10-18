"""
20. JSONデータの読み込み
"""

from c3_common import load_text


def main():
    text: str = load_text("イギリス")
    print(text)


if __name__ == "__main__":
    main()
