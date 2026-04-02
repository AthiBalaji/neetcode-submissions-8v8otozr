class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        h1, h2 = defaultdict(int), defaultdict(int)
        
        for c in t:
            h2[c]+=1
        need = len(h2)
        have = 0 
        l=0 
        res = [-1,-1]
        reslen = float('inf')
        for r in range(len(s)):
            print("l and s[r]",s[l], s[r])
            h1[s[r]]+=1

            if s[r] in h2 and h1[s[r]] == h2[s[r]]:
                have+=1
            
            while have == need:
                h1[s[l]]-=1
                if h1[s[l]] < h2[s[l]] and s[l] in h2:
                    have-=1
                if reslen> r-l+1:
                    reslen = r-l+1
                    res =[l,r]
                l+=1

        l,r = res 
        return s[l:r+1] if reslen != float('inf') else "" 
                    
            
        

