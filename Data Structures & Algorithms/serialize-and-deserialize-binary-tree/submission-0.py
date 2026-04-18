# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(node):
            if not node:
                res.append("N")#mark null
                return 
            res.append(str(node.val))#store value
            #preorder traversal
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)#convert to string 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals=data.split(",")
        self.i=0
        def dfs():
            #handle null
            if vals[self.i]=="N":
                self.i+=1
                return None

            node=TreeNode(int(vals[self.i]))#create node
            self.i+=1

            #rebuild tree in same order(preorder)
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()


