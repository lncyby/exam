#!/usr/bin/python

l = [1,1]

for i in range(20):
    num = l[i] + l[i + 1]
    l.append(num)

print l
