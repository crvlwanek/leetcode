# 1339. Maximum Product of Splitted Binary Tree

def maxProduct(root) -> int:
         
  def subtree_sum(node):
    if not node:
        return
    subtree_sum(node.left)
    subtree_sum(node.right)          
    if node.left:
        node.val += node.left.val
    if node.right:
        node.val += node.right.val

  def largest_product(node):
    if not node:
        return float('-inf')
    current = (root.val - node.val) * node.val
    return max(largest_product(node.left), largest_product(node.right), current)

  subtree_sum(root)
  return max(largest_product(root.left), largest_product(root.right)) % (10**9 + 7)
