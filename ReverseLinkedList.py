from os import *
from sys import *
from collections import *
from math import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    prev=None
    curr=head
    while curr:
        #So that list after curr doesn't get lost
        nxt=curr.next
        #First step of reversal
        curr.next=prev
        #for next iter
        prev=curr
        #for next iter
        curr=nxt
    return prev
        
