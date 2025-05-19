class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
from typing import Optional

def printLinkedList(head: Node) -> str:
    currentNode = head
    linkedList = ""
    while currentNode:
        linkedList += f"{currentNode.val} -> "
        currentNode = currentNode.next
    
    linkedList += "None"
    return linkedList

def dedupSortedList(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(4)
node5 = Node(5)
node6 = Node(5)
node7 = Node(5)
node8 = Node(10)
node9 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9



print(printLinkedList(node1))
print(printLinkedList(dedupSortedList(node1)))