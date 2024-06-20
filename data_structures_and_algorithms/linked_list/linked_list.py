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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if not self.length:
            return None
        elif self.length == 1:
            popped = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return popped
        else:
            cur = self.head
            for _ in range(self.length - 2):
                cur = cur.next
            popped = cur.next.value
            self.tail = cur
            cur.next = None
            self.length -= 1
            return popped

    def prepend(self, value):
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length = 1
        return True

    def pop_first(self):
        popped = None
        if not self.length:
            return popped
        elif self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            popped = self.head
            self.head = popped.next
            popped.next = None

        self.length -= 1
        return popped

    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        else:
            cur = self.head
            for _ in range(idx):
                cur = cur.next
            return cur

    def set(self, idx, value):
        target = self.get(idx)
        if target:
            target.value = value
            return True
        return False

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return False
        elif idx == self.length:
            return self.append(value)
        elif not idx:
            return self.prepend(value)
        new = Node(value)
        temp = self.get(idx - 1)
        new.next = temp.next
        temp.next = new
        self.length += 1
        return True

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        elif idx == self.length - 1:
            return self.pop()
        elif not idx:
            return self.pop_first()

        temp = self.get(idx - 1)
        removed = temp.next
        temp.next = removed.next
        removed.next = None
        self.length -= 1
        return removed

    def reverse(self):
        cur = self.head
        self.head = self.tail
        self.tail = cur

        before = None
        for _ in range(self.length):
            after = cur.next
            cur.next = before
            before = cur
            cur = after


N = LinkedList(11)
N.append(2)

print(N.pop())
print(N.pop())
N.print_all()
