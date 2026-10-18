#! /bin/bash

# -s (stable) を付けて、3列目が同じ行は元の順序を保つ。
FILE_PATH=data/popular-names.txt
sort -s -t $'\t' -k3,3nr $FILE_PATH
