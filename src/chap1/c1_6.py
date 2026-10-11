from c1_5 import get_n_gram


def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"

    X = set(get_n_gram(s=s1, n=2))
    Y = set(get_n_gram(s=s2, n=2))
    
    print(f"{X=}")
    print(f"{Y=}")

    u = X or Y
    i = X and Y
    d = X - Y

    print(f"{u=}")
    print(f"{i=}")
    print(f"{d=}")


if __name__ == "__main__":
    main()
