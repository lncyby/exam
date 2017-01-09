#!/usr/bin/python

class Node(object):
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class Linkdc(object):
    def __init__(self):
        self.head = None

    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next



    def show(self):

        p = self.head.next
        l = []
        stack = []
        while p != None:
            l.append(p.value)
            p = p.next
        print l
        print ""
        for i in l:
            stack.append(i)
            if i == '+':
                o = stack.pop()
                y = stack.pop()
                y = int(y)
                x = stack.pop()
                x = int(x)
                a = x + y
                stack.append(a)
            elif i == '-':
                o = stack.pop()
                y = stack.pop()
                y = int(y)
                x = stack.pop()
                x = int(x)
                a = x - y
                stack.append(a)
            elif i == '*':
                o = stack.pop()
                y = stack.pop()
                y = int(y)
                x = stack.pop()
                x = int(x)
                a = x * y
                stack.append(a)
            elif i == '/':
                o = stack.pop()
                y = stack.pop()
                y = int(y)
                x = stack.pop()
                x = int(x)
                a = x / y
                stack.append(a)
        print stack
