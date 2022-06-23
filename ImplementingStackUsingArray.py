# Stack class.
class Stack:
    def __init__(self, capacity: int):
        self.stack=[]
        self.siz=capacity

    def push(self, num: int) -> None:
        # Write your code here.
        self.stack.append(num)
        

    def pop(self) -> int:
        # Write your code here.
        if len(self.stack)==0:
            return -1
        else:
            return self.stack.pop()
    
    def top(self) -> int:
        # Write your code here.
        if len(self.stack)==0:
            return -1
        else:
            return self.stack[-1]
    
    def isEmpty(self) -> int:
        # Write your code here.
        if len(self.stack)==0:
            return 1
        else:
            return 0
    
    def isFull(self) -> int:
        # Write your code here.
        if len(self.stack)==self.siz:
            return 1
        else:
            return 0
