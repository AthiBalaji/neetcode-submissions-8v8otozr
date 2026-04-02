class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        res = defaultdict(int)
        for i in range(len(nums)):
            res[nums[i]] +=1
        freq = [[] for i in range(len(nums)+1)]

        for q,w in res.items():
            freq[w].append(q)
        o = 0
        for i in range(len(freq)-1,-1,-1):
            if(o==k):
                return result
            for j in freq[i]:
                result.append(j)
                o+=1

        