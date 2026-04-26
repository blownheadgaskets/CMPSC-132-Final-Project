class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def insert(self, value): # Simplified version of insert using a helper method
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:      # This will allow repeated values to be placed in the tree. To avoid this, we do: elif(value>node.value):
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def inorder(self):
        if self.root is None:
            return []
        else:
            return self._inorderHelper(self.root, [])

    def _inorderHelper(self, node, visited):
        if node is not None:
            self._inorderHelper(node.left, visited)
            visited += [node.value]
            self._inorderHelper(node.right, visited)
            return visited

    
    # APPROACH 1 - Calling inorder()
    def kth_smallest_1(self, k):
        list_we_need = self.inorder() #get the inorder list for this BST instance
        if not list_we_need:
            return None
        else:
            return list_we_need[k-1]

    # APPROACH 2 - tree traversal + counter
    def kth_smallest_2(self, k):
        if self.root is None:
            return None    
        self.counter = 0
        return self._kth_helper(self.root, k)


    def _kth_helper(self, node, k):
        #base case, if there is a none or we passed k then return none
        if node ==None or self.counter>k: 
            return None

        #if we find the kth value in the left subtree then return it
        left = self._kth_helper(node.left, k)
        if left is not None:
            return left

        #increment the counter as we go up the tree from the leaf
        self.counter += 1

        #check to see if this is the kth node and return it if it is 
        if self.counter==k:
            return node.value
        
        #if not the current node, search the right subtree
        return self._kth_helper(node.right, k)








    
