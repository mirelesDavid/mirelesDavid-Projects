'''
Time Taken: 40 Minutes
Reasoning

Can make a lot of improvement but ran out of time. Would've liked to create more functions in order
to remove duplicate code.
'''

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def min(self) -> int:
        if not self.root:
            return None
        
        def helper(node: Node) -> int:
            if not node.left:
                return node.val
            
            return helper(node.left)  
        
        return helper(self.root)  
    
    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def max(self) -> int:
        if not self.root:
            return None
        
        def helper(node: Node) -> int:
            if not node.right:
                return node.val
            
            return helper(node.right)  
        
        return helper(self.root)  

    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def getMaxNode(self, node: Node) -> Node:
        if not node:
            return None
        
        def helper(node: Node) -> Node:
            if not node.right:
                return node
            
            return helper(node.right)
        
        return helper(node)

    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def contains(self, val: int) -> bool:
        if not self.root:
            return False
        
        def helper(node: Node) -> bool:
            if not node:
                return False

            if val == node.val:
                return True

            if val > node.val:
                return helper(node.right)
            else:
                return helper(node.left)
            
        return helper(self.root)
    
    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def insert(self, val: int) -> None:
        # Si el árbol está vacío, creamos la raíz
        if not self.root:
            self.root = Node(val)
            return
        
        # Usamos un enfoque recursivo más simple
        def helper(node: Node) -> Node:
            # Si llegamos a una posición vacía, creamos un nuevo nodo
            if not node:
                return Node(val)
            
            # Si el valor ya existe, no hacemos nada
            if val == node.val:
                return node
            
            # Insertamos en el subárbol apropiado y actualizamos los enlaces
            if val > node.val:
                node.right = helper(node.right)
            else:
                node.left = helper(node.left)
            
            # Devolvemos el nodo actual (posiblemente modificado)
            return node
        
        # Iniciamos la recursión desde la raíz
        self.root = helper(self.root)
            
    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def delete(self, val: int) -> bool:
        if not self.root:
            return False
        
        if self.root.val == val and not self.root.left and not self.root.right:
            self.root = None
            return True
        
        def helper(node: Node, prev: Node, isRight: bool, deleteVal: int) -> bool:
            if not node:
                return False

            if deleteVal == node.val:
                #Case 1 node has 2 childs
                if node.left and node.right:
                    #Get the biggest Num in the left subTree
                    newChild = self.getMaxNode(node.left)
                    node.val = newChild.val
                    return helper(node.left, node, False, newChild.val)

                newChild = node.left if node.left else node.right
                
                #Case 2 node has 1 child
                if prev:  
                    if isRight:
                        prev.right = newChild
                    else:
                        prev.left = newChild
                    return True
                
            if deleteVal > node.val:
                return helper(node.right, node, True, deleteVal)
            else:
                return helper(node.left, node, False, deleteVal)
            
        return helper(self.root, None, False, val)



bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(20)
print("Min value:", bst.min()) 
print("Max value:", bst.max())  
print("Contains 7:", bst.contains(7))  
print("Contains 9:", bst.contains(9))  
print("Delete 15:", bst.delete(15))  
print("Contains 15 after delete:", bst.contains(15))  
print("Contains 12 after delete:", bst.contains(12))  
print("Contains 20 after delete:", bst.contains(20))  
print("Delete 10:", bst.delete(10))  
print("Contains 10 after delete:", bst.contains(10))  
print("New min value:", bst.min())  
print("New max value:", bst.max())  