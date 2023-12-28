class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        i, l = 0, len(word)

        while i < l:
            if word[i].isalpha(): i += 1
            else: 
                j=i+1
                while j < l and word[j].isdigit(): j += 1
                nums.add(int(word[i:j]))
                i = j+1
        
        return len(nums)
