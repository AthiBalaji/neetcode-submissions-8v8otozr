class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res =0
        freq_map = defaultdict(int)
        for elem in tasks:
            freq_map[elem] = freq_map[elem]+1
        
        q = len(tasks)
        buckets = [[] for _ in range(q+1)]

        for elem in freq_map:
            buckets[freq_map[elem]].append(elem)

        t =-1

        while True:
            sum =0

            for elem in freq_map:
                sum+=freq_map[elem]
            if sum == 0:
                break
            print("timesss",t, res)
            if t < n and res != 0:
                res += n-t
                t=-1
                print("res", res)
                
            for i in range(len(buckets)-1, -1, -1):
                for elem in buckets[i]:
                    if freq_map[elem] > 0:
                        res+=1
                        print(elem, res)
                        t+=1

                        freq_map[elem]-=1

        
        return res
    




                                          