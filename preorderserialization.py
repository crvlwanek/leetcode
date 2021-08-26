def isValidSerialization(preorder: str) -> bool:
  stack = ["#"]
  for node in preorder.split(","):
    if not stack:
      return False
    stack.pop()
    if node != "#":
      stack.append(node)
      stack.append(node)

  return not stack
