# Singly Linked List Implementation

class SinglyNode:
    """Node for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add element at the end"""
        new_node = SinglyNode(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add element at the beginning"""
        new_node = SinglyNode(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Delete first occurrence of data"""
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def find(self, data):
        """Find element in the list"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        """Display the list"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def size(self):
        """Get size of the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Doubly Linked List Implementation

class DoublyNode:
    """Node for doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Doubly Linked List implementation"""
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """Add element at the end"""
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def prepend(self, data):
        """Add element at the beginning"""
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def delete(self, data):
        """Delete first occurrence of data"""
        current = self.head
        
        while current:
            if current.data == data:
                # If it's the only node
                if current == self.head and current == self.tail:
                    self.head = self.tail = None
                # If it's the head node
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                # If it's the tail node
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                # If it's a middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
    
    def find(self, data):
        """Find element in the list"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display_forward(self):
        """Display the list from head to tail"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def display_backward(self):
        """Display the list from tail to head"""
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements
    
    def size(self):
        """Get size of the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Examples and demonstrations

def demonstrate_singly_linked_list():
    print("=== Singly Linked List Demo ===")
    sll = SinglyLinkedList()
    
    # Adding elements
    print("Adding elements: 1, 2, 3")
    sll.append(1)
    sll.append(2)
    sll.append(3)
    print(f"List: {sll.display()}")
    
    # Prepending element(prepending means adding a new node to the beginning of the list.)
    print("Prepending 0")
    sll.prepend(0)
    print(f"List: {sll.display()}")
    
    # Finding elements
    print(f"Finding 2: {sll.find(2)}")
    print(f"Finding 5: {sll.find(5)}")
    
    # Deleting element
    print("Deleting 2")
    sll.delete(2)
    print(f"List: {sll.display()}")
    
    print(f"Size: {sll.size()}")
    print()

def demonstrate_doubly_linked_list():
    print("=== Doubly Linked List Demo ===")
    dll = DoublyLinkedList()
    
    # Adding elements
    print("Adding elements: 1, 2, 3")
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(f"Forward: {dll.display_forward()}")
    print(f"Backward: {dll.display_backward()}")
    
    # Prepending element
    print("Prepending 0")
    dll.prepend(0)
    print(f"Forward: {dll.display_forward()}")
    print(f"Backward: {dll.display_backward()}")
    
    # Finding elements
    print(f"Finding 2: {dll.find(2)}")
    print(f"Finding 5: {dll.find(5)}")
    
    # Deleting element
    print("Deleting 2")
    dll.delete(2)
    print(f"Forward: {dll.display_forward()}")
    print(f"Backward: {dll.display_backward()}")
    
    print(f"Size: {dll.size()}")
    print()

def compare_performance():
    print("=== Performance Comparison ===")
    print("Operation         | Singly LL | Doubly LL")
    print("------------------|-----------|----------")
    print("Insert at head    | O(1)      | O(1)")
    print("Insert at tail    | O(n)      | O(1)")
    print("Delete at head    | O(1)      | O(1)")
    print("Delete at tail    | O(n)      | O(1)")
    print("Delete middle     | O(n)      | O(n)")
    print("Search            | O(n)      | O(n)")
    print("Traverse forward  | O(n)      | O(n)")
    print("Traverse backward | Not poss. | O(n)")
    print()

if __name__ == "__main__":
    demonstrate_singly_linked_list()
    demonstrate_doubly_linked_list()
    compare_performance()
    
    # Memory usage comparison
    print("=== Memory Usage ===")
    print("Singly Linked List: Each node stores data + 1 pointer (next)")
    print("Doubly Linked List: Each node stores data + 2 pointers (next + prev)")
    print("Trade-off: Doubly linked lists use more memory but offer bidirectional traversal")
