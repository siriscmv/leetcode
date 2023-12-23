class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,cont,i,l=0,0,0,len(nums)
        while (i<l):
            if nums[i]==1: cont+=1
            else:
                if cont>m: m=cont
                cont=0
            i+=1
        return max(m,cont)
