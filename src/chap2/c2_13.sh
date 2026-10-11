#! /bin/bash

FILE_PATH=data/popular-names.txt
N=10
head -n $N $FILE_PATH | tr '\t' ' '
