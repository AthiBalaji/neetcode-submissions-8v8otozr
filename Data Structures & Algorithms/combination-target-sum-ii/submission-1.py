class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            if cur > target or i >=len(candidates):
                return
            path.append(candidates[i])
            cur+=candidates[i]
            dfs(i+1, path, cur)
            path.pop()
            cur-=candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, path, cur)


        dfs(0, [], 0)
        return res