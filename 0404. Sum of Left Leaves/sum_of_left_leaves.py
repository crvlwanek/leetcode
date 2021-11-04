# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    
    def is_leaf(node):
        return not node.left and not node.right
    
    def find_left(node):
        if not node or is_leaf(node):
            return 0
        
        if node.left and is_leaf(node.left):
            return node.left.val + find_left(node.right)
        
        return find_left(node.left) + find_left(node.right)
    
    return find_left(root)