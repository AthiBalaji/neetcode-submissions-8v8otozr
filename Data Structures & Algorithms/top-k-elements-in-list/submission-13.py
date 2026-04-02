class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i_map = defaultdict(int)
        for num in nums:
            i_map[num] +=1
        # print(i_map)
        buckets = [[] for x in range(len(nums)+1)]
        
        for j,v in i_map.items():
            # print("kv",k, v)
            buckets[v].append(j)
        print(buckets)
        result = []
        for i in range(len(buckets)-1,0, -1):
            if len(buckets[i]) != 0:
                for buck in buckets[i]:
                    result.append(buck)
                    k-=1
                    if k == 0:
                        return result
        return result

        