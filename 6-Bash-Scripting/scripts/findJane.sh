#!/bin/bash

:"
chmod +x findJane.sh
files=(`grep 'jane' ./data/list.txt`)
Let's fetch the different fields (columns) using -f flag :
grep " jane " ../data/list.txt | cut -d ' ' -f 1
grep " jane " ../data/list.txt | cut -d ' ' -f 2
grep " jane " ../data/list.txt | cut -d ' ' -f 3
grep ' jane ' ./data/list.txt | cut -d ' ' -f 3 | while read line; do
khjhjh
done
"
files=$(grep ' jane ' ./data/list.txt | cut -d ' ' -f 3 )

for line in $files; do
if test -e ".$line"; then
   echo ".$line" >> ./oldFiles.txt
else
    echo "file dosen't exist : $line";
fi
done


