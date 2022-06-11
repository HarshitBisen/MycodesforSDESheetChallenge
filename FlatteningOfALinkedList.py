from os import *
from sys import *
from collections import *
from math import *

# List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if(self.next):
            del self.next

def mergelist(heada,headb):
    temp=Node(0)
    res=temp
    
    while heada and headb:
        if heada.data<headb.data:
            temp.child=heada
            temp=temp.child
            heada=heada.child
        else:
            temp.child=headb
            temp=temp.child
            headb=headb.child
    if heada:
        temp.child=heada
    else:
        temp.child=headb
    return res.child

def flattenLinkedList(head):
    if head==None or head.next==None:
        return head
    head.next=flattenLinkedList(head.next)
    head=mergelist(head,head.next)
    return head
