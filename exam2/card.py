#!/usr/bin/python

l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
a = len(l)
l1 = []

while a < 14 and a > 1:
    a -= 1
    b = l.pop()
    l1.insert(0,b)
    c = l1.pop()
    l1.insert(0,c)
l1.insert(0,1)
print l1
