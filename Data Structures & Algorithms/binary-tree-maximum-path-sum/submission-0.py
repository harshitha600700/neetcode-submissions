# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(root):
            if not root:
                return 0
            #non-split path
            leftMax=dfs(root.left)
            rightMax=dfs(root.right)
            leftMax=max(0,leftMax)
            rightMax=max(0,rightMax)

            #compute max-path sum with split
            res[0]=max(res[0],root.val+leftMax+rightMax)
            #compute and return max-path sum without split
            return root.val+max(leftMax,rightMax)
        dfs(root)
        return res[0]

        