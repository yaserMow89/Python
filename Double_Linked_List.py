
class Node:
    def __init__(self, data = None, pervious = None, next = None):
        self.data = data
        self.pervious = pervious
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        if self.head == None:
            print("The list is empty")
            return
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        return length

    def insert_at_start(self,data):
        current = self.head
        node = Node(data, pervious=None, next=self.head)
        current.pervious = node
        self.head = node

    def print_list(self):
        current = self.head
        llstr = ""
        count = 1
        while current:
            llstr += str(current.data) + " --> "
            current = current.next
            count += 1
        print(llstr)

ll = DoubleLinkedList()
ll.insert_at_start(1)
ll.insert_at_start(2)
ll.print_list()
ll.insert_at_start(3)
ll.print_list()
# print(ll.get_length())