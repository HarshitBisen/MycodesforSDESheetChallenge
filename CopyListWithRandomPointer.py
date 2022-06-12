from os import *
from sys import *
from collections import *
from math import *

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        

def cloneRandomList(head):
    oldtocopy={None:None}
    cur=head
    
    while cur:
        copy=LinkedListNode(cur.data)
        oldtocopy[cur]=copy
        cur=cur.next
    
    cur=head
    while cur:
        copy=oldtocopy[cur]
        copy.next=oldtocopy[cur.next]
        copy.random=oldtocopy[cur.random]
        cur=cur.next
    return oldtocopy[head]
