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

    def selection_sort(self):
        if self.length < 2:
            return

        curr = self.head

        # while curr.next:
        #     min_node = curr
        #     temp = curr.next

        #     while temp:
        #         if min_node.value > temp.value:
        #             min_node = temp
        #         temp = temp.next

        #     if curr != min_node:
        #         curr.value, min_node.value = min_node.value, curr.value
        #     curr = curr.next

        for i in range(self.length - 1):
            min_node = curr
            temp = curr.next
            for j in range(i + 1, self.length):
                if min_node.value > temp.value:
                    min_node = temp
                temp = temp.next

            if curr != min_node:
                curr.value, min_node.value = min_node.value, curr.value

            curr = curr.next


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""
