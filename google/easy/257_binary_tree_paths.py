
class Node: 
      
    # A binary tree node has data, 
    # pointer to left child and a  
    # pointer to right child 
    def __init__(self, val): 
        self.val = val 
        self.right = None
        self.left = None
class Solution:
    def binaryTreePaths(self, root: Node) :
        path_len = 0
        paths=[]
        path=""


        def get_paths(root,path,path_len,paths):
            if root == None:
                return
           
            path_len +=1
            if root.left == None and root.right == None:
                #print(path)
                path += str(root.val)
                paths.append(path)
                return
            else:
                path += str(root.val) +"->"
                get_paths(root.left,path,path_len,paths)
                get_paths(root.right,path,path_len,paths)
        get_paths(root,path,path_len,paths)
        return paths
        

        
# Driver Code 
root = Node(1); 
root.left = Node(2); 
root.right = Node(3); 
root.left.left = Node(4); 
root.left.right = Node(5); 
sobj = Solution()
sobj.binaryTreePaths(root)


  