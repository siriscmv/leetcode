from collections import deque

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans, vals, curr = 0, deque(), head

        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        while vals:
            a, b = vals.popleft(), vals.pop()
            ans = max(ans, a + b)
        
        return ans
