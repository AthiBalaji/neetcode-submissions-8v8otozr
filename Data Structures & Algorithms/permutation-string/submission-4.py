class Solution:
    def checkInclusion(self,s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        window = {}

        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        have, need = 0, len(count1)
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            window[c] = 1 + window.get(c, 0)

            if c in count1 and window[c] == count1[c]:
                have += 1

            # Keep window size equal to len(s1)
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in count1 and window[left_char] == count1[left_char]:
                    have -= 1
                window[left_char] -= 1
                l += 1

            if have == need:
                return True

        return False
        
        