from collections import deque
import sys

class TreeNode:
    def __init__(self,value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,value): # root 노드에 value 삽입하는 메소드
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(value,self.root) 
    
    def _insert(self,value,cur_node): # recursion을 이용하는 _insert 메소드
        if value < cur_node.value:
            if cur_node.left_child is None: # 현재노드의 왼쪽자식 없는 경우 
                cur_node.left_child = TreeNode(value)
                cur_node.left_child.parent = cur_node # parent 포인터를 설정
            else:
                self._insert(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None: # 현재노드의 오른쪽자식 없는 경우
                cur_node.right_child = TreeNode(value)
                cur_node.right_child.parent = cur_node # parent 포인터를 설정
            else:
                self._insert(value,cur_node.right_child)
        else: # value == cur_node.value
            print("ERR: The value already exists")
            return

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        else:
            print("The tree is None")

    def _print_tree(self,cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value) # Inorder Traverse, Asc
            self._print_tree(cur_node.right_child)
    
    def height(self):
        if self.root is not None:
            return self._height(self.root,0)
        else:
            return 0 

    def _height(self,cur_node,cur_height):
        if cur_node is None: return cur_height
        left_height = self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def search(self,value)->bool:
        if self.root is not None:
            return self._search(value,self.root)
        else:
            return False
    
    def _search(self,value,cur_node)->bool:
        if value < cur_node.value:
            if cur_node.left_child is None:return False
            else:
                print("present tree_value: {} while searching_value: {}, to left_child".format(cur_node.value,value))
                return self._search(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:return False
            else:
                print("present tree_value: {} while searching_value: {}, to right_child".format(cur_node.value,value))
                return self._search(value,cur_node.right_child)
        else: # found
            return True
    
    def find(self,value)->TreeNode:
        if self.root is not None:
            return self._find(value,self.root)
        else:
            return None
    
    def _find(self,value,cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value,cur_node.right_child)
        return None

    def delete_value(self,value): # delete node by value
        return self.delete_node(self.find(value))

    def delete_node(self,node_found):
        def find_RHS_min(node): # RHS에서 가장 작은 값의 노드 == 현재 노드를 대체할 노드
            current = node
            while current.left_child is not None:
                current = current.left_child
            return current

        def num_chil(node): # node의 children 수에 따라 케이스나뉨  
            num = 0
            if node.left_child is not None:num += 1
            if node.right_child is not None: num += 1
            return num

        node_parent = node_found.parent # node_found의 부모
        node_num_chil = num_chil(node_found)

        # case 1) No child
        if node_num_chil == 0:
            if node_parent.left_child == node_found:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # case 2) One child
        elif node_num_chil == 1:
            if node_found.left_child is not None: #found has LHS child
                node_child = node_found.left_child
            else: # found has RHS child
                node_child = node_found.right_child
            
            if node_parent.left_child == node_found: # found is LHS child
                node_parent.left_child = node_child
            else: # found is RHS child
                node_parent.right_child = node_child

        # case 3) Two children
        elif node_num_chil == 2:
            successor = find_RHS_min(node_found) # RHS의 최솟값 갖는 노드를 successor로 
            node_found.value = successor.value # successor의 값을 카피해놓고
            self.delete_node(successor) # successor는 delete

    def bfs_print_tree(self):
        bfs_q = deque()
        if self.root is None:
            print("The tree is empty")
            return None
        else:
            bfs_q.append(self.root) # node를 element로 넣자

            while len(bfs_q) != 0: # q가 empty 아닌동안
                cur_node = bfs_q.popleft()

                print(cur_node.value) # 현재 레벨의 value 출력
                
                # 하위 레벨의 node를 enque
                if cur_node.left_child is not None:bfs_q.append(cur_node.left_child) 
                if cur_node.right_child is not None:bfs_q.append(cur_node.right_child) 


if __name__=="__main__":
    def fill_tree(tree,num_elems=100,max_int=1000):
        from random import randint
        for _ in range(num_elems):
            cur_elem = randint(0,max_int)
            tree.insert(cur_elem)
        return tree

    tree = BST()
    # tree = fill_tree(tree)
    # tree.print_tree()

    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(10)
    tree.insert(9)
    tree.insert(11)
    
    tree.print_tree()

    print("tree height: {}".format(tree.height()))

    # print(tree.search(10))
    # print(tree.search(3))

    # print('---------------------------')
    # tree.delete_value(5)
    # tree.print_tree()
    # print('---------------------------')
    # tree.delete_value(11)
    # tree.print_tree()
    # print('---------------------------')
    # tree.delete_value(9)
    # tree.print_tree()

    tree.bfs_print_tree()


    
