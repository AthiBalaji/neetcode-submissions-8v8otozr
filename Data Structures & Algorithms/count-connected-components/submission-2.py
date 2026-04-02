class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set() 
        connected_components = 0
        nodes = {x:[] for x in range(n)}
        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        def dfs(elem):
            visited.add(elem)
            if nodes[elem] == []:
                return 

            for x in nodes[elem]:
                if x not in visited:
                    dfs(x)
            return 
        result = 0 
        for elem in nodes:
            if elem not in visited:
                print(elem)
                result +=1
                dfs(elem)
        return result 


        