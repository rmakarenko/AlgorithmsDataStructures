class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):

        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all_flag=False):

        previous = self.head

        if previous is None:  # handle empty list
            return

        node = previous.next  # if node is None next while will not start

        if val == previous.value:
            self.head = node
            if self.head is None:
                previous = None
            if all_flag == False:
                if self.head is None:
                    self.tail = None
                return

        while node is not None:
            if node.value == val:
                if self.head == node:
                    self.head = node.next
                previous.next = node.next
                node = node.next
                if self.head is None:
                    previous = None
                if all_flag == False:
                    break
                else:
                    continue
            previous = previous.next
            node = node.next

        if node is None:   # self.tail == node
            self.tail = previous


    def clean(self):
        self.head = None
        self.tail = None

    def len(self):

        if self.head is None:
            return 0
        node = self.head
        count = 1
        while node.next != None:
            node = node.next
            count += 1

        return count

    def insert(self, afterNode, newNode):

        if self.len() == 0:
            
            node_for_insert = Node(newNode)
            node_for_insert.next = None
            self.head = node_for_insert
            self.tail = node_for_insert
            
            return 


        if afterNode is None and self.len() == 0:

            node_for_insert = Node(newNode)
            node_for_insert.next = None
            self.head = node_for_insert
            self.tail = node_for_insert

        elif afterNode is None and self.len() != 0:

            node_ex_head = self.head
            self.head = Node(newNode)
            newNode.next = node_ex_head

        else:
            node_for_insert = Node(newNode)  # создать новый узел
            node = self.head  # найти узел афтернод и сохранить в буфер его следующий элемент, присвоить ему следующий элемент = новый узел

            while node is not None:
                if node.value == afterNode:
                    buffered_item = node.next
                    node.next = node_for_insert
                    node_for_insert.next = buffered_item
                    break
                else:
                    node = node.next

            if self.tail.value == afterNode:
                self.tail = node_for_insert 
    

