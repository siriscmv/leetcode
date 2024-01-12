class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, l = head, 0
        if not head.next: return None

        while curr:
            l += 1
            curr = curr.next
        
        curr, i = head, 0
        for _ in range(l // 2 - 1): curr = curr.next
        
        curr.next = curr.next.next if curr.next else None
        return head
