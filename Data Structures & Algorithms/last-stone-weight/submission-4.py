class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Constraints: 很小 => 桶排序
        # 1 <= stones.length <= 20
        # 1 <= stones[i] <= 100

        #每個桶子代表一種石頭大小(0,1,2,...,100)
        buckets = [0] * 101
        for stone in stones:
            buckets[stone] += 1

        fst = 100
        scd = 100 
        
        while fst > 0:
            buckets[fst] %= 2
            # 整除的話繼續走 
            if buckets[fst] == 0:
                fst -= 1
                continue

            # 找到 fir後來找scd
            scd = min(fst - 1, scd)
            while scd > 0 and buckets[scd] == 0:
                scd -= 1

            # 沒有第二顆了 直接回傳第一顆
            if scd == 0:
                return fst
            # 找到的話 各減一顆
            buckets[fst] -= 1
            buckets[scd] -= 1
            diff = fst - scd
            if diff > 0:
                buckets[diff] += 1
            # 刷新fst
            fst = max(diff, scd)
        return 0