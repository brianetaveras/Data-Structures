"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length == 0:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head.value
        new_node = ListNode(value, None, None)
        current_head = self.head
        new_node.next = current_head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self.head.value
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        old_val = self.head.value
        self.head.next.prev = None
        self.head = None
        self.length -= 1
        return old_val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == 0:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head.value
        if self.length == 1:
            current_tail = self.tail
            new_node = ListNode(value, current_tail, None)
            new_node.prev.next = new_node
            self.head.next = new_node
            self.tail = new_node
            self.length += 1
            return self.head.value
        new_node = ListNode(value, None, None)
        old_val = self.tail.value
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return old_val
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.tail == None
            self.head = None
            self.length -= 1
            return
        old_val = self.tail.value
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail
        self.length -= 1
        return old_val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            return
        current = self.head
        while current.next is not node:
            current = current.next
        if current.next is not node:
            return
        current.next.prev = current
        current.next = current.next.next 
        self.add_to_head(node)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.next is None:
            return
        current = self.head
        while current.next is not self.tail:    
            current = current.next
        if current.next is not node:
            return
        current.next.next.prev = current
        current.next = current.next.next
        self.add_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return 
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            print(f"here: {self.length}")
            return
        current = self.head
        while current.next is not node:
            current = current.next
        current.next.next.prev = current
        current.next = current.next.next
        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return 0
        if self.length ==1:
            return self.head.value
        max_val = 0
        current = self.head
        while current.next is not None:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        if current.value > max_val:
            max_val = current.value
        
        return max_val

