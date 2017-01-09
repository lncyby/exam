#!/bin/bash

for i in {1..10}
do
  let "num += $i "
done

echo $num
