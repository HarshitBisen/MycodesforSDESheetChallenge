from os import *
from sys import *
from collections import *
from math import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    c=0
    t=head
    while t!=None:
        c+=1
        t=t.next
    if c%2!=0:
        d=c//2
        p=head
        while d:
            p=p.next
            d-=1
        return p
    else:
        d=(c//2)
        q=head
        while d:
            q=q.next
            d-=1
        return q
            
