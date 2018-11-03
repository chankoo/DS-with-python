class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node()
    
    def enque(self,data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def deque(self):

        if self.head.next is None:
            # print('ERR: The queue is empty!!!')
            return -1
        else:
            pop_node = self.head.next
            self.head.next = pop_node.next
            return pop_node.data

    def disp(self):
        tmp = []
        self
        cur = self.head.next
        if cur is None:
            print([])
            return
        while cur.next is not None:
            tmp.append(cur.data)
            cur = cur.next
        tmp.append(cur.data)
        print(tmp)


    def size(self):

        cnt = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            cnt += 1
        print(cnt)
        return cnt

    def empty(self):
        if self.head.next is None:
            print(1)
        else:
            print(0)
    
    def front(self):
        if self.head.next is None:
            print(-1)
        else:
            print(self.head.next.data)

    def back(self):
        if self.head.next is None:
            print(-1)
        else:
            cur_node = self.head.next
            while cur_node.next is not None:
                cur_node = cur_node.next
            print(cur_node.data)

if __name__=='__main__':
    q1 = Queue()
    q1.enque(1)
    q1.enque(2)

    print(q1.deque())

