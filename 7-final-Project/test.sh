#!/bin/bash

# grep -w "INFO\|ERROR" "./syslog.log" | head | cut -d' ' -f7- |  sort | sort -nr
# awk "/INFO|ERROR/" "./syslog.log" | head | cut -d' ' -f7- |  sort
declare -A err_msgs

lines=$(cat './syslog.log' | cut -d' ' -f7- | sort | sort -nr)
#readarray -t lines <  "./syslog.log"
#for _line in "${lines[@]}"; do

while IFS== read -r _line; do
 # lline=$( echo $_line | cut -d' ' -f7-)
  rm_username=${_line/(*)/}
  rm_bracket=${rm_username/\[*\]/}
  cleanText=$(echo $rm_bracket | tr -d '\n' | sed 's/ *$//g')

  if [[ -v err_msgs[$cleanText]  ]]; then
    ((err_msgs[$cleanText]++))
  elif [[ ! -v err_msgs[$cleanText] ]]; then
    err_msgs[$cleanText]=1
 fi
done  <<< "$lines"


#echo "map file to built in array indext:................................... "
#mapfile MyFile < './syslog.log'
#printf '%s' "${MyFile[@]:5}"

echo "iterate over both keys and values ################################################################"
# iterate over both keys and values
for key in "${!err_msgs[@]}"; do
  echo "$key : ${err_msgs[$key]} "
done

echo "iterate over keys only ################################################################"
# iterate over keys only
for key in "${!err_msgs[@]}"; do
  echo $key
done