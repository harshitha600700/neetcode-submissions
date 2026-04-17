# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #iterative inorder traversal
        n=0
        stack=[]
        cur=root
        while cur or stack:#continue if we either hv nodes to explore or nodes in stack
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur=cur.right
        