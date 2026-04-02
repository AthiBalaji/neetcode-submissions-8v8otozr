class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}
        for string in strs:
            l = [0]*26

            for c in string:
                l[ord(c)-ord('a')] += 1
            anagmap = tuple(l)
            if anagmap in res:
                res[anagmap].append(string)
            else:
                res[anagmap] = []
                res[anagmap].append(string)
        res = list(res.values())
        return res
