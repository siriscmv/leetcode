class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []

        while head:
            nodes.append(head.val)
            head = head.next
        
        return nodes == nodes[::-1]
