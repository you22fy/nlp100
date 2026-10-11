import random


def main():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    r = []
    for si in s.split():
        if len(si) <= 4:
            r.append(si)
            continue

        part = list(si[1:-1])
        random.shuffle(part)
        r.append(si[0] + "".join(part) + si[-1])

    print(" ".join(r))


if __name__ == "__main__":
    main()
