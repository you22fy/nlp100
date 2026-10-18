#! /bin/bash

# macOS には shuf が無いので、無ければ sort -R で代用する。
FILE_PATH=data/popular-names.txt
if command -v shuf > /dev/null 2>&1; then
    shuf $FILE_PATH
else
    sort -R $FILE_PATH
fi
