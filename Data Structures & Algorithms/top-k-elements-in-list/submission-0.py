class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 找相同 => hashmap => key: num value: 次數
        hashmap = dict()
        for num in  nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # 找出 k 大 => 最小堆積（Min-Heap）
        heap = []
        for k_num, v_times in hashmap.items(): 
            # .items => dict 變成 tuple 陣列

            # 要heap 可是每個元素又要帶有一個副加資訊 
            # => 把元素跟副加資訊 做成tuple
            # 以出現次數(v_times)為依據堆疊, 復加資訊是數字(k_num)
            tuple1 = (v_times, k_num)
            heapq.heappush(heap,tuple1)
            if len(heap) > k:
                heapq.heappop(heap)

        return [k_num for v_times, k_num in heap]




        