# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      if not head: return head
      l, curr, prev = 0, head, None
      while curr: 
        prev = curr
        curr = curr.next
        l += 1
      prev.next = head
      
      k, curr = l - k % l, head
      for _ in range(k-1): curr = curr.next
      head = curr.next
      curr.next = None
      return head
