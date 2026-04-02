class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        bucket = [[] for i in range(len(nums))]
        for num in nums:
            res[num] =  1+res.get(num,0)
        
        for num,freq in res.items():
            bucket[freq-1].append(num)

        result =[]
        for i in range(len(bucket)-1, -1, -1):
            for c in bucket[i]:
                result.append(c)
                if(len(result) == k):
                    return result