class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList():
    def printLinkedList(head: Node) -> str:
        currentNode = head
        linkedList = ""
        while currentNode:
            linkedList += f"{currentNode.val} -> "
            currentNode = currentNode.next
        
        linkedList += "None"
        return linkedList
    
    def insertAtFront(head: Node, val: int) -> Node:
        newNode = Node(val, head)
        return newNode
    
    def insertAtBack(head: Node, val: int) -> Node:
        if not head:
            return Node(val)
        
        currentNode = head
        prev = None
        while currentNode:
            prev = currentNode
            currentNode = currentNode.next
        
        newNode = Node(val)
        prev.next = newNode
        return head

    def insertAfter(head: Node, val: int, loc: Node) -> Node:
        newNode = Node(val)
        
        newNode.next = loc.next
        loc.next = newNode
        
        return head

    def insertBefore(head: Node, val: int, loc: Node) -> Node:    
        currentNode = head
        newNode = Node(val)
        prevNode = None
        
        if currentNode == loc:
            prevNode = newNode
            prevNode.next = currentNode
            return prevNode
        
        while currentNode:
            if currentNode == loc:
                newNode.next = currentNode
                prevNode.next = newNode
                return head
            
            prevNode = currentNode
            currentNode = currentNode.next
        
    def deleteFront(head: Node) -> Node:
        head = head.next
        return head

    def deleteBack(head: Node) -> Node:
        currentNode = head
        
        if not currentNode.next:
            return None
        
        prev = None
        while currentNode.next:
            prev = currentNode
            currentNode = currentNode.next
        
        prev.next = None
        return head
            
    
    def deleteNode(head: Node, loc: Node) -> Node:
        currentNode = head
        prev = None
        
        if currentNode == loc:
            head = head.next
            return head
        
        
        while currentNode:
            if currentNode == loc:
                prev.next = currentNode.next
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
            node.next = prev
            prev = node
            
            helper(nxt)
        
        prev = None
        helper(head)
        return prev
            


# Test cases for all methods

# 1. insertAtFront
# Test case 1: Insert into empty list
head = None
print("Before insertAtFront(None, 5):", "None")
head = SingleLinkedList.insertAtFront(head, 5)
print("After insertAtFront(None, 5):", SingleLinkedList.printLinkedList(head))

# Test case 2: Insert at front of list with one element
print("Before insertAtFront(head, 10):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertAtFront(head, 10)
print("After insertAtFront(head, 10):", SingleLinkedList.printLinkedList(head))

# Test case 3: Insert at front of list with multiple elements
print("Before insertAtFront(head, 15):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertAtFront(head, 15)
print("After insertAtFront(head, 15):", SingleLinkedList.printLinkedList(head))

# 2. insertAtBack (Note: This method has bugs in the implementation)
# Test case 1: Insert into empty list
head = None
print("\nBefore insertAtBack(None, 5):", "None")
head = SingleLinkedList.insertAtBack(head, 5)
print("After insertAtBack(None, 5):", SingleLinkedList.printLinkedList(head) if head else "None")

# Test case 2: Insert at back of list with one element
head = Node(10)
print("Before insertAtBack(head, 20):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertAtBack(head, 20)
print("After insertAtBack(head, 20):", SingleLinkedList.printLinkedList(head))

# Test case 3: Insert at back of list with multiple elements
head = Node(10, Node(20))
print("Before insertAtBack(head, 30):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertAtBack(head, 30)
print("After insertAtBack(head, 30):", SingleLinkedList.printLinkedList(head))

# 3. insertAfter
# Test case 1: Insert after the only node
head = Node(5)
print("\nBefore insertAfter(head, 10, head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertAfter(head, 10, head)
print("After insertAfter(head, 10, head):", SingleLinkedList.printLinkedList(head))

# Test case 2: Insert after the first node in a multi-node list
head = Node(5, Node(15))
print("Before insertAfter(head, 10, head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertAfter(head, 10, head)
print("After insertAfter(head, 10, head):", SingleLinkedList.printLinkedList(head))

# Test case 3: Insert after the last node
head = Node(5, Node(10))
last_node = head.next
print("Before insertAfter(head, 15, last_node):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertAfter(head, 15, last_node)
print("After insertAfter(head, 15, last_node):", SingleLinkedList.printLinkedList(head))

# 4. insertBefore
# Test case 1: Insert before the head
head = Node(10)
print("\nBefore insertBefore(head, 5, head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertBefore(head, 5, head)
print("After insertBefore(head, 5, head):", SingleLinkedList.printLinkedList(head))

# Test case 2: Insert before the second node
head = Node(5, Node(15))
second_node = head.next
print("Before insertBefore(head, 10, second_node):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertBefore(head, 10, second_node)
print("After insertBefore(head, 10, second_node):", SingleLinkedList.printLinkedList(head))

# Test case 3: Insert before a middle node
head = Node(5, Node(10, Node(20)))
middle_node = head.next
print("Before insertBefore(head, 7, middle_node):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.insertBefore(head, 7, middle_node)
print("After insertBefore(head, 7, middle_node):", SingleLinkedList.printLinkedList(head))

# 5. deleteFront
# Test case 1: Delete from a list with one node
head = Node(5)
print("\nBefore deleteFront(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteFront(head)
print("After deleteFront(head):", SingleLinkedList.printLinkedList(head) if head else "None")

# Test case 2: Delete from a list with two nodes
head = Node(5, Node(10))
print("Before deleteFront(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteFront(head)
print("After deleteFront(head):", SingleLinkedList.printLinkedList(head))

# Test case 3: Delete from a list with multiple nodes
head = Node(5, Node(10, Node(15)))
print("Before deleteFront(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteFront(head)
print("After deleteFront(head):", SingleLinkedList.printLinkedList(head))

# 6. deleteBack
# Test case 1: Delete from a list with one node
head = Node(5)
print("\nBefore deleteBack(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteBack(head)
print("After deleteBack(head):", SingleLinkedList.printLinkedList(head) if head else "None")

# Test case 2: Delete from a list with two nodes
head = Node(5, Node(10))
print("Before deleteBack(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteBack(head)
print("After deleteBack(head):", SingleLinkedList.printLinkedList(head))

# Test case 3: Delete from a list with multiple nodes
head = Node(5, Node(10, Node(15)))
print("Before deleteBack(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteBack(head)
print("After deleteBack(head):", SingleLinkedList.printLinkedList(head))

# 7. deleteNode
# Test case 1: Delete the head node
head = Node(5, Node(10))
print("\nBefore deleteNode(head, head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteNode(head, head)
print("After deleteNode(head, head):", SingleLinkedList.printLinkedList(head))

# Test case 2: Delete a middle node
head = Node(5, Node(10, Node(15)))
middle_node = head.next
print("Before deleteNode(head, middle_node):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteNode(head, middle_node)
print("After deleteNode(head, middle_node):", SingleLinkedList.printLinkedList(head))

# Test case 3: Delete the last node
head = Node(5, Node(10, Node(15)))
last_node = head.next.next
print("Before deleteNode(head, last_node):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.deleteNode(head, last_node)
print("After deleteNode(head, last_node):", SingleLinkedList.printLinkedList(head))

# 8. length
# Test case 1: Empty list
head = None
print("\nLength of empty list:", SingleLinkedList.length(head))

# Test case 2: List with one node
head = Node(5)
print("Length of list", SingleLinkedList.printLinkedList(head), ":", SingleLinkedList.length(head))

# Test case 3: List with multiple nodes
head = Node(5, Node(10, Node(15, Node(20))))
print("Length of list", SingleLinkedList.printLinkedList(head), ":", SingleLinkedList.length(head))

# 9. reverseIterative
# Test case 1: Reverse a list with one node
head = Node(5)
print("\nBefore reverseIterative(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseIterative(head)
print("After reverseIterative(head):", SingleLinkedList.printLinkedList(head))

# Test case 2: Reverse a list with two nodes
head = Node(5, Node(10))
print("Before reverseIterative(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseIterative(head)
print("After reverseIterative(head):", SingleLinkedList.printLinkedList(head))

# Test case 3: Reverse a list with multiple nodes
head = Node(5, Node(10, Node(15)))
print("Before reverseIterative(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseIterative(head)
print("After reverseIterative(head):", SingleLinkedList.printLinkedList(head))

# Test case 1: Reverse an empty list
head = None
print("\nBefore reverseRecursive(head):", "None")
head = SingleLinkedList.reverseRecursive(head)
print("After reverseRecursive(head):", SingleLinkedList.printLinkedList(head) if head else "None")

# Test case 2: Reverse a list with one node
head = Node(5)
print("\nBefore reverseRecursive(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseRecursive(head)
print("After reverseRecursive(head):", SingleLinkedList.printLinkedList(head))

# Test case 3: Reverse a list with two nodes
head = Node(5, Node(10))
print("\nBefore reverseRecursive(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseRecursive(head)
print("After reverseRecursive(head):", SingleLinkedList.printLinkedList(head))

# Test case 4: Reverse a list with multiple nodes
head = Node(5, Node(10, Node(15, Node(20))))
print("\nBefore reverseRecursive(head):", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseRecursive(head)
print("After reverseRecursive(head):", SingleLinkedList.printLinkedList(head))

# Test case 5: Reverse, then reverse again to get back original list
head = Node(5, Node(10, Node(15)))
print("\nOriginal list:", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseRecursive(head)
print("After first reverseRecursive:", SingleLinkedList.printLinkedList(head))
head = SingleLinkedList.reverseRecursive(head)
print("After second reverseRecursive (should match original):", SingleLinkedList.printLinkedList(head))