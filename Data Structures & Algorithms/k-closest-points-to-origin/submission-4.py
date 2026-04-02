class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for elem in points:
            distance = (elem[0]**2 + elem[1]**2)**(0.5)
            print("elem and distane", elem, distance)
            t = (elem, distance)
            result.append(t)
        res = sorted(result, key = lambda x:x[1])
        print("soretedadsa", res)
        ans = []
        j =0 
        while k!=0:
            print("result", res[j][0])
            ans.append(res[j][0])
            j+=1
            k-=1
        return ans
        