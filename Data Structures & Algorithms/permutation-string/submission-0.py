class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = [0]*26
        s2_map = [0]*26

        for i in range(len(s1)):
            s1_map[ord(s1[i])-ord('a')]+=1
            s2_map[ord(s2[i])-ord('a')]+=1

        matches = 0 
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches+=1
        print(matches)    
        l = 0 
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True 
            if s2_map[ord(s2[r])- ord('a')] == s1_map[ord(s2[r])- ord('a')]:
                matches -=1 
            s2_map[ord(s2[r]) -ord('a')]+=1
            if s2_map[ord(s2[r]) -ord('a')] == s1_map[ord(s2[r])- ord('a')]:
                matches+=1
            if s2_map[ord(s2[l])- ord('a')] == s1_map[ord(s2[l])- ord('a')]:
                matches -=1 
            s2_map[ord(s2[l]) -ord('a')]-=1
            if s2_map[ord(s2[l]) -ord('a')] == s1_map[ord(s2[l])- ord('a')]:
                matches+=1
            l+=1
        return matches == 26            



        
        
        
        

        
        