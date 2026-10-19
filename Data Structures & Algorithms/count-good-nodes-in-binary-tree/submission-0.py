# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        if not root:
            return 0
        def rec(node,max_node):
            nonlocal ans
            if node is None:
                return
            if node.val>=max_node:
                ans+=1
            max_node=max(max_node,node.val)
            rec(node.left,max_node)
            rec(node.right,max_node)
            return ans
        return rec(root,root.val)