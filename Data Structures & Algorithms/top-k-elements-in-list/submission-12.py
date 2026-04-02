class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resmap = {}
        for elem in nums:
            if elem in resmap:
                resmap[elem]+=1
            else:
                resmap[elem] = 1

        freqlist = [[] for i in range(len(nums)+1)]
        enu = resmap.items()
        for i,j in enu:
            freqlist[j].append(i)
        
        resultlist = []
        for elem in reversed(freqlist):
            if elem:
                for e in elem:
                    resultlist.append(e)
                    k-=1

            if(k==0):
                break
        return resultlist


        