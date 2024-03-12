class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, start = 0, ListNode(0, head)
        node_map, curr = dict(), start
        node_map[s] = start

        while curr:
            s += curr.val
            node_map[s] = curr
            curr = curr.next

        curr, s = start, 0
        while curr:
            s += curr.val
            curr.next = node_map[s].next
            curr = curr.next

        return start.next
