class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if not self.length:
            return None
        elif self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):
        if not self.length:
            return self.append(value)
        else:
            new = Node(value)
            new.next = self.head
            self.head.prev = new
            self.head = new
            self.length += 1
            return True

    def pop_first(self):
        if not self.length:
            return None

        elif self.length == 1:
            return self.pop()

        else:
            popped = self.head
            self.head = popped.next
            self.head.prev = None
            popped.next = None

            self.length -= 1
            return popped

    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None

        if idx < self.length / 2:
            cur = self.head
            for _ in range(idx):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.length - idx - 1):
                cur = cur.prev
        return cur

    def set_value(self, idx, value):
        target = self.get(idx)
        if target:
            target.value = value
            return True
        return False

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return False
        elif not idx:
            return self.prepend(value)
        elif idx == self.length:
            return self.append(value)
        else:
            new = Node(value)
            before = self.get(idx - 1)
            after = before.next

            before.next = new
            new.prev = before
            new.next = after
            after.prev = new

            self.length += 1
            return True

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        elif not idx:
            return self.pop_first()
        elif idx == self.length - 1:
            return self.pop()
        else:
            removed = self.get(idx)

            removed.next.prev = removed.prev
            removed.prev.next = removed.next
            removed.next = None
            removed.prev = None

            self.length -= 1
            return removed
