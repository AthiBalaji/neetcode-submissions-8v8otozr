class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        his_visit = set() 
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False 
            elif preMap[crs] == []:
                return True 
            visit.add(crs)
            for elem in preMap[crs]:

                if not dfs(elem):
                    return False
            visit.remove(crs)
            # preMap[crs] = []
            return True 


        for crs in preMap:
            if not dfs(crs):
                return False 
        return True 