class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head
        
        a, b = head, head.next
        even_head = b
        
        while b and b.next:
            a.next = b.next
            a = a.next
            b.next = a.next
            b = b.next

        a.next = even_head
        return head
