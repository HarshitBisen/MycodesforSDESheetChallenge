from os import *
from sys import *
from collections import *
from math import *

'''
    class Node :
        def __init__(self, data) :
            self.data = data
            self.next = None
'''

def detectCycle(head) :
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False
