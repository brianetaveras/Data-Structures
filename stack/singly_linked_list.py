#!/usr/bin/env python3

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    def __str__(self):
        pass

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0
    def __str__(self):
        return f"LinkedList with {self.length} elements"

    def add_to_head(self, value):
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            print(f'added {value}')
            return
        old_head = self.head
        self.head = Node(value, old_head)
        self.length += 1
        print(f'added {value}')

    def remove_head(self):
        if self.head is None:
            return None
        if self.length == 1:
            old_val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return old_val
        old_head = self.head
        self.head = old_head.next
        self.length -= 1
        return old_head.value
    def add_to_tail(self, value):
        if self.length == 0:
            new_tail = Node(value, None)
            self.tail = new_tail
            self.head = new_tail
            self.length += 1
            return
        new_tail = Node(value, None)
        self.tail.next = new_tail
        self.tail = new_tail
        self.length += 1

    def remove_tail(self):
        if self.length == 0:
            return 0
        if(self.length == 1):
            old_val = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return old_val
        current = self.head
        while current.next is not self.tail:
            current = current.next
        
        old_val = current.next.value
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return old_val
        


        
        

