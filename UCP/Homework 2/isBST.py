class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

def isBST(root: Optional[Node]) -> bool:
    if not root:
        return True
    
    def dfs(node: Optional[Node], lowerBound: int, upperBound: int) -> bool:
        if not node:
            return True
        
        if not (lowerBound < node.val and node.val < upperBound):
            return False

        return dfs(node.left, lowerBound, node.val) and dfs(node.right, node.val, upperBound)

    return dfs(root, float("-inf"), float("inf"))


root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(15)

print(isBST(root))