class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #反向排列拿最大
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            l = -heapq.heappop(stones)
            l_sec = -heapq.heappop(stones)

            if l > l_sec:
                l = l - l_sec    
                heapq.heappush(stones, -l) 
        
        return -stones[0] if stones else 0
        