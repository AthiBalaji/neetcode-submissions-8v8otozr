class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            n = len(s)
            prefix = str(n) + "#"
            encoded_str += prefix + s
        print(encoded_str)
        return encoded_str



    def decode(self, s: str) -> List[str]:
        res = []
        l = "" 
        k = 0 
        while k != len(s): 
          c = s[k]
          if c == "#":
            q = int(l)
            res.append(s[k+1:k+1+q])
            k+=q+1
            l=""
            continue
          l+=c
          k+=1
        return res 

        
        
