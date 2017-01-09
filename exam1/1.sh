#!/bin/bash

array=(1 2 3 4 5 6)
# read array

for i in "${array[@]}"
do
  let "num = $i % 2"
  if  [ $num -eq 0 ]
  then
    echo "$i"
  fi
done

echo ""
