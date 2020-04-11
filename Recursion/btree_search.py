'''
Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.  

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.


'''

# A binary tree node 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
    def printBT(self,root):
        current = root
        stack = []

        while True:
            if current != None:
                stack.append(current)
                current = current.left
            elif(stack):
                current =stack.pop()
                print(current.data, end=' ')
                current = current.right
            else:
                break
    #binary tree search with recursion.
    #feel free to submit better version
    def findNode(self,root,val):

        def findNode2(root,val):
            if root == None or root.data == val:
                return root
            if root.data < val:
                return findNode2(root.right,val)
            return findNode2(root.left,val)
        temp = findNode2(root,val)
        return temp





root = Node(4) 
root.left = Node(2) 
root.right = Node(7) 
root.left.left = Node(1) 
root.left.right = Node(3) 

root.printBT(root)
print()
result = root.findNode(root,2)
root.printBT(result)
  

