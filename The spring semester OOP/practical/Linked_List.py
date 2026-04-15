class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end = "->")
            current_node = current_node.next
        print("None")

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return  #这里空链表直接返回，避免后续的逻辑不断重复
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node



llist = LinkedList()
llist.append(5)
llist.append(6)
llist.prepend(10)
llist.prepend(50)
llist.print_list()

def remove_duplicates_with_buffer(head):
    if not head:
        return head
    seen = set()
    current = head
    seen.add(current.data)

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return head