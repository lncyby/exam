#!/usr/bin/python

def max(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j],l[j + 1] = l[j + 1],l[j]
    print(l)

p = [2,9,4,6,3,8,1,5]
max(p)
