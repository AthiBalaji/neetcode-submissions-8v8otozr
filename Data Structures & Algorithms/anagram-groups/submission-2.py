class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Damap = defaultdict(list)
        for st in strs:
            count = [0]*26
            for c in st:
                count[ord(c) - ord('a')] +=1
            Damap[tuple(count)].append(st)
        return list(Damap.values())
            

