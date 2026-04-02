class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        course_map = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            course_map[crs].append(pre)
        
        visited = set()
        called = set()
        res = []
        appended = set()

        def dfs(elem):
            called.add(elem)

            if course_map[elem] == []:
                if elem not in appended:
                    res.append(elem)
                    appended.add(elem)

                visited.remove(elem)
                return True 


            for x in course_map[elem]:
                if x in visited: 
                    return False
                visited.add(x)
                if not dfs(x):
                    return False
            course_map[elem] = []
            if elem not in appended:
                res.append(elem)
                appended.add(elem)
            visited.remove(elem)
            return True


        for elem in course_map:
            if elem not in called:
                visited.add(elem)
                if not dfs(elem):
                    return []
        return res 
                


