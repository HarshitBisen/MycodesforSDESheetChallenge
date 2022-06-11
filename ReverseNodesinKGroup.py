from os import *
from sys import *
from collections import *
from math import *

# Following is the class structure of the Node class:   
class Node:
    def __init__(self, data):
       	self.data = data
        self.next = None

def getListAfterReverseOperation(head, n, b):
    b = [i for i in b if i != 0]
    n=len(b)
    if head==None or n==0:
        return head
    Next=None
    curr=head
    prev=None
    count=0
    n-=1
    while curr!=None and count<b[0]:
        Next=curr.next
        curr.next=prev
        prev=curr
        curr=Next
        count+=1
    if Next!=None and n>0:
        b.remove(b[0])
        head.next=getListAfterReverseOperation(Next, n, b)
    if n==0:
        head.next=Next
    return prev
