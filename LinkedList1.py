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

        target_node = None
        if self.len() == 0:
            self.head = Node(newNode)
            self.tail = self.head
        else:
            target_node = self.find(afterNode)
        if target_node is None:
            return
        target_next = target_node.next
        target_node.next = Node(newNode)
        target_node.next.next = target_next
        if target_next is None:
            self.tail = target_node.next    
   

