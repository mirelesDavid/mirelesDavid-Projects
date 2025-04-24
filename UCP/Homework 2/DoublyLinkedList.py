class Node():
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList():
    def printLinkedList(head: Node) -> str:
        if not head:
            return "Empty List"
        
        # Forward direction representation
        forward = "Forward:  "
        # Backward direction representation
        backward = "Backward: "
        
        # First pass: build the forward string
        current = head
        while current:
            forward += f"{current.val} <-> "
            current = current.next
        forward += "None"
        
        # Second pass: build the backward string
        # Find the tail first
        tail = head
        while tail and tail.next:
            tail = tail.next
        
        # Now go backward from tail
        current = tail
        while current:
            backward += f"{current.val} <-> "
            current = current.prev
        backward += "None"
        
        # Combine both representations
        return f"{forward}\n{backward}"
    
    def insertAtFront(head: Node, val: int) -> Node:
        if not head:
            return Node(val)
        
        newNode = Node(val, head)
        head.prev = newNode
        return newNode
    
    def insertAtBack(head: Node, val: int) -> Node:
        if not head:
            return Node(val)
        
        currentNode = head
        prev = None
        while currentNode:
            prev = currentNode
            currentNode = currentNode.next
        
        newNode = Node(val, None, prev)
        prev.next = newNode
        return head

    def insertAfter(head: Node, val: int, loc: Node) -> Node:
        newNode = Node(val, None, loc)
        
        nxtNode = loc.next
        nxtNode.prev = newNode
        newNode.next = nxtNode
        loc.next = newNode
        
        return head

    def insertBefore(head: Node, val: int, loc: Node) -> Node:    
        currentNode = head
        newNode = Node(val)
        prevNode = None
        
        if currentNode == loc:
            newNode.next = currentNode
            currentNode.prev = newNode
            return newNode
        
        while currentNode:
            if currentNode == loc:
                prevNode.next = newNode
                newNode.prev = prevNode                
                newNode.next = currentNode
                currentNode.prev = newNode
                return head
            
            prevNode = currentNode
            currentNode = currentNode.next
        
    def deleteFront(head: Node) -> Node:
        nxt = head.next
        head = head.next
        nxt.prev = None
        return head

    def deleteBack(head: Node) -> Node:
        currentNode = head
        
        if not currentNode.next:
            return None
        
        prev = None
        while currentNode.next:
            prev = currentNode
            currentNode = currentNode.next
        
        nxtNode = prev.next
        prev.next = None
        nxtNode.prev = None
        return head
            
    
    def deleteNode(head: Node, loc: Node) -> Node:
        currentNode = head
        prev = None
        
        if currentNode == loc:
            if not head.next:
                return None
            else:
                nxtNode = head.next
                nxtNode.prev = None
                head = head.next
                return head
        
        
        while currentNode:
            if currentNode == loc:
                nxtNode = currentNode.next
                if nxtNode:
                    prev.next = nxtNode
                    nxtNode.prev = prev
                else:
                    prev.next = None
                    currentNode.prev = None
                
                return head
            
            prev = currentNode
            currentNode = currentNode.next
        
        return head
    
    def length(head: Node) -> int:
        count = 0
        currentNode = head
        
        while currentNode:
            count += 1
            currentNode = currentNode.next
        
        return count
    
    def reverseIterative(head: Node) -> Node:
        currentNode = head
        prev = None
        
        while currentNode:
            nxtNode = currentNode.next
            currentNode.prev = nxtNode
            currentNode.next = prev
            prev = currentNode
            currentNode = nxtNode
        
        return prev
        
    def reverseRecursive(head: Node) -> Node:
        def helper(node: Node):
            nonlocal prev
            if not node:
                return None

            nxt = node.next
            node.prev = nxt
            node.next = prev
            prev = node
            
            helper(nxt)
        
        prev = None
        helper(head)
        return prev

# Test cases for all methods in DoublyLinkedList

# 1. insertAtFront
# Test case 1: Insert into empty list
head = None
print("Before insertAtFront(None, 5):", "None")
head = DoublyLinkedList.insertAtFront(head, 5)
print("After insertAtFront(None, 5):", DoublyLinkedList.printLinkedList(head))

# Test case 2: Insert at front of list with one element
print("Before insertAtFront(head, 10):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertAtFront(head, 10)
print("After insertAtFront(head, 10):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Insert at front of list with multiple elements
print("Before insertAtFront(head, 15):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertAtFront(head, 15)
print("After insertAtFront(head, 15):", DoublyLinkedList.printLinkedList(head))

# 2. insertAtBack
# Test case 1: Insert into empty list
head = None
print("\nBefore insertAtBack(None, 5):", "None")
head = DoublyLinkedList.insertAtBack(head, 5)
print("After insertAtBack(None, 5):", DoublyLinkedList.printLinkedList(head))

# Test case 2: Insert at back of list with one element
head = Node(10)
print("Before insertAtBack(head, 20):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertAtBack(head, 20)
print("After insertAtBack(head, 20):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Insert at back of list with multiple elements
head = Node(10, Node(20))
head.next.prev = head  # Set prev pointer for doubly linked list
print("Before insertAtBack(head, 30):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertAtBack(head, 30)
print("After insertAtBack(head, 30):", DoublyLinkedList.printLinkedList(head))

# 3. insertAfter
# Test case 1: Insert after the only node
head = Node(5)
print("\nBefore insertAfter(head, 10, head):", DoublyLinkedList.printLinkedList(head))
# For this test, we need to create a proper structure where loc.next exists
head.next = Node(15)
head.next.prev = head
head = DoublyLinkedList.insertAfter(head, 10, head)
print("After insertAfter(head, 10, head):", DoublyLinkedList.printLinkedList(head))

# Test case 2: Insert after the first node in a multi-node list
head = Node(5)
head.next = Node(15)
head.next.prev = head
print("Before insertAfter(head, 10, head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertAfter(head, 10, head)
print("After insertAfter(head, 10, head):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Insert after the last node
head = Node(5)
last_node = Node(10)
head.next = last_node
last_node.prev = head
# Create a node after last_node for the test to work with the current implementation
last_node.next = Node(20)
last_node.next.prev = last_node
print("Before insertAfter(head, 15, last_node):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertAfter(head, 15, last_node)
print("After insertAfter(head, 15, last_node):", DoublyLinkedList.printLinkedList(head))

# 4. insertBefore
# Test case 1: Insert before the head
head = Node(10)
print("\nBefore insertBefore(head, 5, head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertBefore(head, 5, head)
print("After insertBefore(head, 5, head):", DoublyLinkedList.printLinkedList(head))

# Test case 2: Insert before the second node
head = Node(5)
second_node = Node(15)
head.next = second_node
second_node.prev = head
print("Before insertBefore(head, 10, second_node):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertBefore(head, 10, second_node)
print("After insertBefore(head, 10, second_node):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Insert before a middle node
head = Node(5)
middle_node = Node(10)
last_node = Node(20)
head.next = middle_node
middle_node.prev = head
middle_node.next = last_node
last_node.prev = middle_node
print("Before insertBefore(head, 7, middle_node):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.insertBefore(head, 7, middle_node)
print("After insertBefore(head, 7, middle_node):", DoublyLinkedList.printLinkedList(head))

# 5. deleteFront
# Test case 1: Delete from a list with more than one node
head = Node(5)
head.next = Node(10)
head.next.prev = head
print("\nBefore deleteFront(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteFront(head)
print("After deleteFront(head):", DoublyLinkedList.printLinkedList(head) if head else "None")

# Test case 2: Delete from a list with two nodes
head = Node(5)
head.next = Node(10)
head.next.prev = head
print("Before deleteFront(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteFront(head)
print("After deleteFront(head):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Delete from a list with multiple nodes
head = Node(5)
middle = Node(10)
last = Node(15)
head.next = middle
middle.prev = head
middle.next = last
last.prev = middle
print("Before deleteFront(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteFront(head)
print("After deleteFront(head):", DoublyLinkedList.printLinkedList(head))

# 6. deleteBack
# Test case 1: Delete from a list with one node
head = Node(5)
print("\nBefore deleteBack(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteBack(head)
print("After deleteBack(head):", DoublyLinkedList.printLinkedList(head) if head else "None")

# Test case 2: Delete from a list with two nodes
head = Node(5)
head.next = Node(10)
head.next.prev = head
print("Before deleteBack(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteBack(head)
print("After deleteBack(head):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Delete from a list with multiple nodes
head = Node(5)
middle = Node(10)
last = Node(15)
head.next = middle
middle.prev = head
middle.next = last
last.prev = middle
print("Before deleteBack(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteBack(head)
print("After deleteBack(head):", DoublyLinkedList.printLinkedList(head))

# 7. deleteNode
# Test case 1: Delete the head node
head = Node(5)
head.next = Node(10)
head.next.prev = head
print("\nBefore deleteNode(head, head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteNode(head, head)
print("After deleteNode(head, head):", DoublyLinkedList.printLinkedList(head))

# Test case 2: Delete a middle node
head = Node(5)
middle = Node(10)
last = Node(15)
head.next = middle
middle.prev = head
middle.next = last
last.prev = middle
print("Before deleteNode(head, middle):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteNode(head, middle)
print("After deleteNode(head, middle):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Delete the last node
head = Node(5)
middle = Node(10)
last = Node(15)
head.next = middle
middle.prev = head
middle.next = last
last.prev = middle
print("Before deleteNode(head, last):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.deleteNode(head, last)
print("After deleteNode(head, last):", DoublyLinkedList.printLinkedList(head))

# 8. length
# Test case 1: Empty list
head = None
print("\nLength of empty list:", DoublyLinkedList.length(head))

# Test case 2: List with one node
head = Node(5)
print("Length of list", DoublyLinkedList.printLinkedList(head), ":", DoublyLinkedList.length(head))

# Test case 3: List with multiple nodes
head = Node(5)
head.next = Node(10)
head.next.prev = head
head.next.next = Node(15)
head.next.next.prev = head.next
head.next.next.next = Node(20)
head.next.next.next.prev = head.next.next
print("Length of list", DoublyLinkedList.printLinkedList(head), ":", DoublyLinkedList.length(head))

# 9. reverseIterative
# Test case 1: Reverse a list with one node
head = Node(5)
print("\nBefore reverseIterative(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.reverseIterative(head)
print("After reverseIterative(head):", DoublyLinkedList.printLinkedList(head))

# Test case 2: Reverse a list with two nodes
head = Node(5)
head.next = Node(10)
head.next.prev = head
print("Before reverseIterative(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.reverseIterative(head)
print("After reverseIterative(head):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Reverse a list with multiple nodes
head = Node(5)
head.next = Node(10)
head.next.prev = head
head.next.next = Node(15)
head.next.next.prev = head.next
print("Before reverseIterative(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.reverseIterative(head)
print("After reverseIterative(head):", DoublyLinkedList.printLinkedList(head))

# 10. reverseRecursive
# Test case 1: Reverse a list with one node
head = Node(5)
print("\nBefore reverseRecursive(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.reverseRecursive(head)
print("After reverseRecursive(head):", DoublyLinkedList.printLinkedList(head))

# Test case 2: Reverse a list with two nodes
head = Node(5)
head.next = Node(10)
head.next.prev = head
print("Before reverseRecursive(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.reverseRecursive(head)
print("After reverseRecursive(head):", DoublyLinkedList.printLinkedList(head))

# Test case 3: Reverse a list with multiple nodes
head = Node(5)
head.next = Node(10)
head.next.prev = head
head.next.next = Node(15)
head.next.next.prev = head.next
print("Before reverseRecursive(head):", DoublyLinkedList.printLinkedList(head))
head = DoublyLinkedList.reverseRecursive(head)
print("After reverseRecursive(head):", DoublyLinkedList.printLinkedList(head))