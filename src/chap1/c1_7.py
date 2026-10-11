def main():
    x, y, z = 12, "気温", 22.4
    r = template(x=x, y=y, z=z)
    print(r)

def template(x,y,z) -> str:
    return f"{x}時の{y}は{z}"

if __name__ == "__main__":
    main()