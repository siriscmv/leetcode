class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        return prev
