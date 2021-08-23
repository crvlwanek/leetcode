# 653. Two Sum IV - Input is a BST

def findTarget(root: Optional[TreeNode], k: int) -> bool:
        
  def check_node(node, seen=set()):
    if not node:
      return False
    if node.val in seen:
      return True

    seen.add(k - node.val)

    return check_node(node.left, seen) or check_node(node.right, seen)

  return check_node(root)
