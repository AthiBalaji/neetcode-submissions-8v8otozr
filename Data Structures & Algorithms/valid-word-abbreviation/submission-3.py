class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r = 0, 0 
        n, m = len(word), len(abbr)
        
        while l < n and r < m:
            if abbr[r].isdigit():
                if abbr[r] == '0':
                    return False 
                k = r
                res = ""
                while k < m and abbr[k].isdigit():
                    res+=abbr[k]
                    k+=1
                # if l+int(res) > n -1:
                #     return False 
                l += int(res)
                r = k 
                continue
            if abbr[r] != word[l]:
                return False
            else:
                l+=1
                r+=1

        return l == n and r == m 


        