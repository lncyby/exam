#!/usr/bin/python

class Node(object):
    def __init__(self,val,p = None):
        self.value = val
        self.p = p
        self.prior = None

class Linklist(object):
    def __init__(self):
        self.head = None

    def __getitem__(self,key):
        return self.getitem(key)

    def __setitem__(self,key,value):
        self.delete(key)
        return self.insert(key,value)

    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)

            p.next = node
            node.prior = p
            p = p.next
        p.next = self.head
        self.head.prior = p

    def show(self):
        p = self.head.next

        while p != self.head:
            print p.value,
            p = p.next
        print ""

    def insert(self,index,value):
        p = self.head
        j = 0
        while p.next != self.head and j < index:
            p = p.next
            j += 1
        q = Node(value)
        q.next = p.next
        p.next.prior = q
        p.next = q
        q.prior = p

    def delete(self,index):
        p = self.head
        i = 0
        while p != self.head and i < index:
            p = p.next
            i += 1
            p.next = p.next.next
            p.next.prior = p

    def getitem(self,index):

        i = 0
        p = self.head.next

        while p != None and i < index:
            i += 1
            p = p.next

        if p == None:
            return -1
        else:
            return p.value

l = Linklist()

l.initlist([1,2,3,4,5])
l.show()

l.insert(3,10)
l.show()

l.delete(2)
l.show()

print l[2]

l[4] = 20
l.show()
