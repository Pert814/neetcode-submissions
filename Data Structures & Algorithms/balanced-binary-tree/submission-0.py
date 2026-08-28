# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node):
            if not node:
                return 0
            left = get_depth(node.left)
            right = get_depth(node.right)
            if left == -1 or right == -1:
                return -1
            if diff(left, right) > 1:
                return -1
            return 1 + max(left, right)
        
        def diff(a: int,b: int) -> int:
            if a > b:
                return a-b
            elif a < b:
                return b-a
            else:
                return 0
        
        depth = get_depth(root)
        if depth == -1:
            return False
        else:
            return True
        