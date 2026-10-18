#! /bin/bash

FILE_PATH=data/popular-names.txt
cut -f 1 $FILE_PATH | sort | uniq
