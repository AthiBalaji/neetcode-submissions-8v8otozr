class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)  
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            print(first, second, second - first)
            first = second - first
            if first > 0:
                heapq.heappush(heap, -first)
        
        
        return -heap[0] if len(heap) == 1 else 0 
