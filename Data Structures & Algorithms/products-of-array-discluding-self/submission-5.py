import math
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #product=math.prod(nums)
        n=len(nums)
        product=[0]*n
        for i in range(n):
            # if nums[i]!=0:
            #     prod=1
            #     nums[i]=[x*prod for x in nums if x!=0]
            # else:
            #     nums[i]=product
            if i==0:
                product[i]=math.prod(nums[1:])
            elif i==n-1:
                product[i]=math.prod(nums[:i])
            else:
                product[i]=math.prod(nums[:i])*math.prod(nums[i+1:])
        return product   
        