class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node()

    def push(self,data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        return

    def display(self):
        els = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            els.append(cur_node.data)
        print(els)

    def size(self):
        cnt = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            cnt += 1
        return cnt

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def pop(self):
        if self.empty==1:
            print("ERR: The stack is empty!!!")
            print(-1)
            return None
        else:
            cur_node = self.head
            while cur_node.next is not None:
                last_node = cur_node
                cur_node = cur_node.next
            last_node.next = None
            print(cur_node.data)
            return cur_node.data

    def top(self):
        if self.empty==1:
            print(-1)
            return None
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            print(cur_node.data)

if __name__ == '__main__':
    s = Stack()
    
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.display()
    s.top()
    