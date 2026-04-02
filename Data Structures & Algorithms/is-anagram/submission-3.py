class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for c in s:
            s_map[c] = s_map.get(c,0) + 1
        for c in t:
            t_map[c] = t_map.get(c,0) + 1
        # if s_map == t_map:
        #     return True
        # else:
        #     return False
        return True if s_map == t_map else False
        
        