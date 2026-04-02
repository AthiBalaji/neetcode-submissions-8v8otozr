class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs = [0]*26
        ft = [0]*26 

        for c in s:
            ascii = ord(c)-ord('a')
            fs[ascii] +=1

        for c in t:
            ascii = ord(c)-ord('a')
            ft[ascii] +=1
        if ft == fs:
            return True 
        else:
            return False




        