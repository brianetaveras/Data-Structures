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
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head.value
        self.head.prev = new_node
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node
        self.length += 1
        return self.head.value
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return
        if self.head is self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        old_head = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        
        return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = None
        self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return
        if self.length == 1:
            old_val = self.tail.value
            self.tail = None
            self.head = None
            self.length -= 1
            return old_val
        old_tail = self.tail
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail
        self.length -= 1
        return old_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)
    

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None:
            return
        if node.prev is None:
            self.remove_from_head()
            return node.value
        if node.next is None:
            self.remove_from_tail()
            return node.value
        
        current_node = self.head

        while current_node is not node:
            print(current_node.value)
            current_node = current_node.next
        # print(f"FOUND YOU {current_node.value}") 
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        self.length -= 1
        current_node = None

        
    """ 
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        if self.length == 1:
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

node = ListNode(1)
list = DoublyLinkedList(node)



list.delete(node)


list.add_to_tail(10)


list.add_to_head(9)


list.add_to_tail(6)



list.delete(list.head.next)

print(list.head.next.value, list.tail.value)
print(list.head.value)