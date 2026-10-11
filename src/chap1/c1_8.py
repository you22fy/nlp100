def main():
    s = "This is an English message"
    r = cipher(s)
    print(r)


def cipher(s):
    CODE_a = ord("a")
    CODE_z = ord("z")
    az_code_sum = CODE_a + CODE_z
    text = [chr(az_code_sum - ord(w)) if CODE_a <= ord(w) <= CODE_z else w for w in s]
    return "".join(text)


if __name__ == "__main__":
    main()
