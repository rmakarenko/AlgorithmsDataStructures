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
