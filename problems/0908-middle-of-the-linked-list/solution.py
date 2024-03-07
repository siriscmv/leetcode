class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast:
            if fast.next: fast = fast.next.next
            else: break
            
            slow = slow.next
        
        return slow
