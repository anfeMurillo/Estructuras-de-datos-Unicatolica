class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None 

    def push(self, value):
        node = LinkedListNode(value)  
        node.next = self.head         
        self.head = node             

    def pop(self):
        if self.head is None:  
            return None
        value = self.head.value  
        self.head = self.head.next 
        return value  
    
    def get_elements(self):
        elements = []
        current = self.head
        while current is not None: 
            elements.append(current.value)
            current = current.next
        return elements

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None

    def enqueue(self, value):
        node = LinkedListNode(value)  
        if self.tail is None:  
            self.head = node
            self.tail = node
        else:
            self.tail.next = node 
            self.tail = node       

    def dequeue(self):
        if self.head is None:  
            return None
        value = self.head.value  
        self.head = self.head.next  
        if self.head is None: 
            self.tail = None
        return value 

    def get_elements(self):
        elements = []
        current = self.head
        while current is not None: 
            elements.append(current.value)
            current = current.next
        return elements

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Lista")
print(s.get_elements())
print("Eliminados")
print(s.pop())  # 30
print(s.pop())  # 20
print(s.pop())  # 10
print("Lista")
print(s.get_elements())

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Cola")
print(q.get_elements())
print("Eliminados")
print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue()) 
print("Cola")
print(q.get_elements())
