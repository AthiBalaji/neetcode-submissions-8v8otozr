class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        unique = set()
        l=0
        for r in range(len(s)):
            while(s[r] in unique):
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            counter = max(counter, r-l+1)
            

        return counter