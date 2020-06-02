'''270 Closest Binary Search Tree Value
k = search tree value
diff = difference


'''
class Node: 
      
    # A binary tree node has data, 
    # pointer to left child and a  
    # pointer to right child 
    def __init__(self, val): 
        self.val = val 
        self.right = None
        self.left = None
class Solution:
    def binaryTreeSearch(self, root: Node,k) :
        #k,diff,answer
        cache = [k,k,k]
        
        def get_closest_val(root,cache):
            if root == None:
                return 
            if root.val == cache[0]:
                cache[2] = root.val
                cache[1] = 0
                return
            diff  = abs(root.val - cache[0])
            if diff < cache[1]:
                    cache[2] = root.val
                    cache[1] = diff
            if root.left == None and root.right == None:
                return
            else:   
                get_closest_val(root.left,cache)
                get_closest_val(root.right,cache)
        get_closest_val(root,cache)
        print( cache)
        

        
# Driver Code 
root = Node(1); 
root.left = Node(2); 
root.right = Node(3); 
root.left.left = Node(4); 
root.left.right = Node(5); 
sobj = Solution()
k=8
sobj.binaryTreeSearch(root,k)


  