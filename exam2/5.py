#!/usr/bin/python
#coding=utf-8

class Node(object):
    def __init__(self,val,next = None):
        self.value = val
        self.next = next

class Linklist(object):
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
        while p != None:
            print p.value,
            p = p.next

        print ""

    def clear(self):
        self.head = None

    def append(self,value):
        p = self.head
        while p.next != None:
            p = p.next
        p.next = Node(value)

    def insert(self,index,value):

        p = self.head

        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1

        q = Node(value)
        q.next = p.next
        p.next = q

        self.delete(index + 1)

    def delete(self,index):

        p = self.head
        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1

        if p.next == None:
            print "index is error"
        else:
            p.next = p.next.next
    def index(self,value):

        p = self.head.next
        i = 0
        while p != None and not (p.value == value):
            p = p.next
            i += 1

        if p == None:
            return -1
        else:
            return i


l = Linklist()

l.initlist([1,2,3,4,5])
l.show()

print "增加"
l.append(10)
l.show()
print "改"
l.insert(2,30)
l.show()

print "删"
l.delete(3)
l.show()

print "查"
print l.index(30)
