class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, lst):
        other = lst.head

        dummy = Node(0)
        current = dummy

        while self.head and other:
            if self.head.value < other.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other
                other = other.next
            current = current.next

        if self.head:
            current.next = self.head
        else:
            current.next = other
            self.tail = lst.tail

        self.head = dummy.next
        self.length += lst.length


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
