class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element  

    def get_position(self, position):
        count = 1
        current = self.head
        while current:
            if count == position:
                return current
            current = current.next
            count += 1

    def print(self):
        current = self.head
        llstr = ""
        while current:
            llstr += str (current.value) + " --> "
            current = current.next
        print(llstr)
    
    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
            
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                break
            current = current.next
    
    # def insert(self, new_element, position):


    def insert(self, new_element, position):
        tempElement = self.get_position(position)
        self.get_position(position-1).next = new_element
        new_element.next = tempElement

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.insert(e4,3)
ll.print()