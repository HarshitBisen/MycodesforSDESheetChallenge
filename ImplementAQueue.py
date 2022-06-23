class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.q=[]




    '''----------------- Public Functions of Queue -----------------'''

   
    def isEmpty(self) :
        #Implement the isEmpty() function
        if len(self.q)==0:
            return True
        else:
            return False



    def enqueue(self, data) :
        #Implement the enqueue(element) function
        self.q.append(data)
        



    def dequeue(self) :
        #Implement the dequeue() function
        if len(self.q)==0:
            return -1
        else:
            t=self.q[0]
            self.q.remove(t)
            return t



    def front(self) :
        #Implement the front() function
        if len(self.q)==0:
            return -1
        else:
            return self.q[0]
