# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sumRootToLeaf1(root: Optional[TreeNode]) -> int:
        
    def helper(root):
        if not root:
            return []

        if not root.left and not root.right:
            return [(root.val, 1)]

        return [(leafVal + root.val * 2**leafLevel, leafLevel + 1) for leafVal, leafLevel in [*helper(root.left), *helper(root.right)]]
    
    return sum(val for val, _ in helper(root))

def sumRootToLeaf2(root: Optional[TreeNode]) -> int:
    
    def dfs(num, root):
        
        if not root:
            return 0
        
        num = num << 1 | root.val
        if not root.left and not root.right:
            return num
        
        return dfs(num, root.left) + dfs(num, root.right)
    
    return dfs(0, root)