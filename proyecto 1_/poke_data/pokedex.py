from poke_data.node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def show_list(self):
        if self.is_empty():
            return "List is empty"

        current_node = self.head
        string = ""
        while current_node:
            string += f"{current_node.data.name}\n" 
            current_node = current_node.next
        return string

    def seach_by_position(self, cant):
        if not self.head:
            return None

        current = self.head
        for i in range(cant):

            current = current.next

        return current.data

    def is_empty(self):
        return self.head is None

    def add_to_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_head(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def remove_from_tail(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None

    def search(self, name):
        if not self.head:  
            return None

        current = self.head
        while current:
            if current.data.name == name:
                return current.data  
            current = current.next

        return None  