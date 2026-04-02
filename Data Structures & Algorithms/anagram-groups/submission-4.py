class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            count = [0]*26
            for c in strs[i]:
                count[ord(c)-ord('a')]+=1
            if(tuple(count) not in res):
                res[tuple(count)] = [strs[i]]
            else:
                res[tuple(count)].append(strs[i])
        return list(res.values()) 
        