def main():
    s: str = "I am an NLPer"
    s.replace(" ", "")

    print(s)

    tg: list[str] = get_n_gram(s=s, n=3)
    bg: list[str] = get_n_gram(s=s, n=2)
    print(f"{tg=}")
    print(f"{bg=}")

def get_n_gram(s: str, n: int) -> list[str]:
    """文字N-gramを得る"""
    l: list[str] = []
    for i in range(len(s) - n + 1):
        l.append(s[i:i + n])
    
    return l


if __name__ == "__main__":
    main()
