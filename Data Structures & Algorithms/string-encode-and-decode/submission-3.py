class Solution:

    def encode(self, strs: List[str]) -> str:
        newarr = [0] * len(strs)
        for i in range(len(strs)):
            newarr[i] = str(len(strs[i])) + '#' + strs[i]
        encoded = "".join(newarr)
        return encoded

    def decode(self, s: str) -> List[str]:
        lenstr = len(s)
        decoded = []
        i = 0
        while i < lenstr:
            # Find the length of the next string
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Length of the next string
            i = j + 1  # Skip the '#' character
            
            # Append the string (empty or not)
            decoded.append(s[i:i + length])
            i += length  # Move to the next part of the string
        
        return decoded
