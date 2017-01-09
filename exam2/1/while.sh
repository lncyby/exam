#!/bin/bash

i=1

while((i<=10))
do
  let "sum += i"
  let "i += 1"
done
echo $sum
