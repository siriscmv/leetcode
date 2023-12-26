class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [char.lower() for char in s if char.isalnum()]
        i, j = 0, len(chars)-1

        while (i <= j):
            if chars[i] != chars[j]: return False
            i += 1
            j -= 1
        
        return True
