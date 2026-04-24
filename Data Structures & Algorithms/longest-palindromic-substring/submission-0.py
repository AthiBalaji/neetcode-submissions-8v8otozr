class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reslen = 0 
        res_idx = 0 
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True 
                    if j-i+1 > reslen:
                        reslen = j-i+1
                        res_idx = i 
        return s[res_idx:res_idx+reslen]