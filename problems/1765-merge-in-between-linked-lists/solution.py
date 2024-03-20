class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i, curr = 0, list1

        while i < a-1: 
            curr = curr.next
            i += 1
        
        nxt = curr.next
        curr.next = list2
        curr = nxt

        while i < b:
            curr = curr.next
            i += 1
        
        end = list2
        while end.next: end = end.next

        end.next = curr
        return list1
