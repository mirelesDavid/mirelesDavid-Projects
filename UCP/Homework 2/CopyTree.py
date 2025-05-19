class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

def copyBST(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return None
    
    newNode = Node(root.val)
    newNode.left = copyBST(root.left)
    newNode.right = copyBST(root.right)
    
    return newNode

def print_tree_simple(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * level + prefix + str(root.val))
        if root.left or root.right:
            print_tree_simple(root.left, level + 1, "L--- ")
            print_tree_simple(root.right, level + 1, "R--- ")
            

root = Node(5, Node(10), Node(15))
copied = copyBST(root)

assert copied != root