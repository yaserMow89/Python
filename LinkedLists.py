## Linked List
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data) ## None is optional 
            return
        itr = self.head
        while itr.next:
            itr = itr.next        
        itr.next = Node(data) ## None is optional
        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            if itr.next:
                llstr += str(itr.data) + ' --> '
            else:
                llstr += str(itr.data)    
            itr = itr.next
        print (llstr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def remove_at(self, index):
        if 0 > index or index > self.get_length():
            raise Exception ("Invalid Index")
        if index == 0:
            self.head= self.head.next
            return
        count = 0
        itr = self.head
        while count < index:
            if count + 1 == index:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0 
        itr = self.head
        
        while itr:

            if count + 1 == index:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            

def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert)
            return
        
        itr = self.head
        while itr:
            if data_after == itr.data:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
