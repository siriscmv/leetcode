from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, ll = head, deque() 
        
        while curr:
          ll.append(curr)
          curr = curr.next
        
        head = curr = None
        while len(ll) >= 2:
          a, b = ll.popleft(), ll.pop()
          b.next = None
          a.next = b
          if not curr: curr = a
          else: 
            curr.next = a
            curr = curr.next
          curr = curr.next
          
        if ll:
          a = ll.pop()
          a.next = None
          if curr: curr.next = a
          else: curr = a
        
        return head
