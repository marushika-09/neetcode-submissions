class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        i=0
        keys=[]
        while i<k:
            top_key = counts.most_common(1)[0][0] if counts else None
            keys.append(top_key)
            del counts[top_key]
            i+=1
        return keys    