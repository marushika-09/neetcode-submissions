class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for i in s:
            if i-1 not in s:
                length=1
                current= i
                while current+1 in s:
                    length+=1
                    current+=1
                longest=max(longest,length)         
                    
        return longest      
        