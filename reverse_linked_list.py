# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

def reverseListIter(head: Optional[ListNode]) -> Optional[ListNode]:
  prev = None
  while head:
    _next = head.next
    head.next = prev
    prev = head
    head = _next
  return prev

def reverseListRecur(head: Optional[ListNode]) -> Optional[ListNode]:

  def reverse(prev, curr):
    head = reverse(curr, curr.next) if curr.next else curr
    curr.next = prev
    return head

  return reverse(None, head) if head else head
