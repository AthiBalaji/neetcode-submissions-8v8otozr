class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        freq = Counter(tasks)
        
        freq_list = [0]*26

        heap = []
        for elem in freq:
            if freq[elem] > 0:
                heap.append(freq[elem])
        heap.sort()


        t = 0
        while heap or queue:
            t+=1
            flag = 0 
            if heap:
                flag = 1 
                task = heap.pop()
                task-=1

            if flag and task and task != 0:
                queue.append((task, t+n+1))

            if queue and queue[0][1] == t+1:
                new_avail = queue.popleft()
                heap.append(new_avail[0])
                heap.sort()

        return t 



                                          