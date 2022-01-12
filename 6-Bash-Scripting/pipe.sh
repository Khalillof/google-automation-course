#!/bin/bash

cat syslog.log | tail | grep 'INFO'  >> info.log
cat syslog.log | sort | uniq -c| grep 'INFO'  >> info.log | cat info.log | tail

cat syslog.log | grep 'INFO' | sort -nr | tail -5
 cat syslog.log | grep 'INFO' | head | cut -d' ' -f7- |  sort | sort -nr

 ##########################################################################