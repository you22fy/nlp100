#! /bin/bash

# GNU split なら `split -n l/$N` で済むが、macOS (BSD split) には無いので
# 1ファイルあたりの行数 (切り上げ) を計算して -l で分割する。
FILE_PATH=data/popular-names.txt
N=10
PREFIX=data/split_sh_

TOTAL=$(wc -l < $FILE_PATH)
LINES=$(( (TOTAL + N - 1) / N ))
split -d -l $LINES -a 2 $FILE_PATH $PREFIX

ls ${PREFIX}*
