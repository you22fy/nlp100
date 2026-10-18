#! /bin/bash

# 出現頻度の降順、同数なら名前の昇順。
FILE_PATH=data/popular-names.txt
cut -f 1 $FILE_PATH | sort | uniq -c | sort -k1,1nr -k2,2
