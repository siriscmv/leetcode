class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        stack = []
        while x > 0:
          stack.append(x%10)
          x//=10
        i, j = 0, len(stack)-1

        while i<j:
          if stack[i] != stack[j]: return False
          i += 1
          j -= 1
        return True
