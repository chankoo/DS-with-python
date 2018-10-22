class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        cnt = 0
        while cur.next is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def display(self):
        els = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            els.append(cur.data)
        print(els)

    def get(self, idx):
        if idx >= self.length():
            print("Index Out of Range!!!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == idx:
                return cur_node.data
            cur_idx += 1

    def pop(self, idx):
        if idx >= self.length():
            print("ERR: Index Out of Range!!!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == idx:
                last_node.next = cur_node.next
                del cur_node
                return
            cur_idx += 1

    def remove(self, data):
        cur_node = self.head
        while cur_node.next is not None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                last_node.next = cur_node.next
                del cur_node
                return
        print("ERR: data is not in the list!!!")

    def insert(self, idx, data):
        if idx >= self.length():
            print("ERR: Index Out of Range!!!")
            return None
        new_node = Node(data)
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next

            if cur_idx == idx:
                last_node.next = new_node
                new_node.next = cur_node
                return

            cur_idx += 1