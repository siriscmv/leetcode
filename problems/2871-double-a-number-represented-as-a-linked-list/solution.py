class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
      curr, digits, carry = head, [], 0
      while curr:
        digits.append(curr)
        curr = curr.next
      
      for i, node in enumerate(digits[::-1]):
        node.val = node.val * 2 + carry
        if node.val >= 10: 
          node.val %= 10
          carry = 1
        else: carry = 0
      
      if not carry: return head
      return ListNode(carry, head)
