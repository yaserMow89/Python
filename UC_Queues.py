

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        current = self.storage
        new_ele = Queue(new_element)

        pass

    def peek(self):
        pass 

    def dequeue(self):
        pass

    q1 = Queue()
    print(type(q1.storage))