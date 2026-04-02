class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        l =0 
        charmap = {}
        res = 0
        for r in range(len(s)):
            if s[r] in charmap and charmap[s[r]]>= l:
                l = charmap[s[r]]+1
                charmap[s[r]] = r
                continue
            else:
                charmap[s[r]] = r
                res = max(res,r-l+1)
        return res





        
        