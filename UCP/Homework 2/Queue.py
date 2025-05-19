class Node():
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def peek(self) -> int:
        if not self.isEmpty():
            return self.left.next.val
        return None
    
    def enqueue(self, x: int) -> None:
        newNode = Node(x)
        lastNode = self.right.prev
        
        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.right
        self.right.prev = newNode
    
    def dequeue(self) -> int:
        if self.isEmpty():
            return None
        
        nodeToRemove = self.left.next
        nxtNode = nodeToRemove.next
        self.left.next = nxtNode
        nxtNode.prev = self.left
        
        return nodeToRemove.val
    
    def isEmpty(self) -> bool:
        return self.left.next == self.right


queue = Queue()
print(queue.isEmpty())
queue.enqueue(10)
queue.enqueue(5)
print(queue.peek())
queue.enqueue(20)
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
queue.dequeue()
print(queue.peek())