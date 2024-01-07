class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      return self.solve(l1, l2, 0)

    def solve(self, l1, l2, c):
      if not l1 and not l2 and not c: return None
      if not l1: l1 = ListNode(0)
      if not l2: l2 = ListNode(0)

      s = l1.val + l2.val + c
      return ListNode(s % 10, self.solve(l1.next, l2.next, 0 if s < 10 else 1))
