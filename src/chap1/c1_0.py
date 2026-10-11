"""
パタトクカシーー
"""

def main():
    p: str = "パトカー"
    t: str = "タクシー"

    r: str = ''
    for pi, ti in zip(p, t):
        r += pi + ti
    
    print(r)

if __name__ == "__main__":
    main()