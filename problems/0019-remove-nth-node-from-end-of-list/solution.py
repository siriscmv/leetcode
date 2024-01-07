# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

      l, curr = 0, head
      while curr: 
        curr = curr.next
        l += 1
      
      curr, j = head, l - n
      if j == 0: return head.next
      for _ in range(j-1): curr = curr.next
      
      if j == l: curr.next = None
      else: curr.next = curr.next.next
      return head
