#!/usr/bin/python

def fun(c):
    l = c.split(' ')
    c = ''.join(l)
    l = c.split('-')
    c = ''.join(l)
    return c

while True:
    s = raw_input()
    if not len(s):
        break

    s = fun(s)

    print s
