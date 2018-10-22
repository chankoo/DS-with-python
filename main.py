from linked_list import LinkedList
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.display()

    print(my_list.get(0))

    my_list.pop(1)
    my_list.display()
    my_list.remove(3)
    my_list.display()
    my_list.insert(1,10)
    my_list.display()
