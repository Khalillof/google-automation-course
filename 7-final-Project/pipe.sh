#!/bin/bash
#chmod +x pipe.sh

cat syslog.log | tail | grep 'INFO'  >> info.log
cat syslog.log | sort | uniq -c| grep 'INFO'  >> info.log | cat info.log | tail

cat syslog.log | grep 'INFO' | sort -nr | tail -5

cat syslog.log | grep 'INFO' | head | cut -d' ' -f7- |  sort | sort -nr
#####################################################

liner=" :......................................................."
echo "read words $liner"
rst=`cat test.txt`;
for i in $rst; do
  echo $i
done

echo "read line by line $liner"
cat test.txt | while read line; do
echo $line
done

echo "reading wrord from grep result $liner"

for i in `grep 'Friday' test.txt`; do
  echo $i
done

echo "reading ines from grep22 result $liner"

grep 'Tuesday' test.txt | while read line; do
  echo $line
done

echo $liner

for jfile in  `cat ./data/list.txt`; do
  echo $jfile
done

echo $liner

for logfile in /var/log/*log; do
   echo "processing : $logfile"
#   cut -d ' ' -f5 $logfile | sort | uniq -c | sort -nr | head -5
done