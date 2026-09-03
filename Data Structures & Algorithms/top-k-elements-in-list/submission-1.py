class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 桶排序 => 如果用數字當作桶子編號 => 數字沒有限制 會有無限的桶子
        # 但如果改用"次數"當桶子編號 => 上限 len(nums) + 1 
        hashmap = dict()
        for num in  nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for k_num, v_times in hashmap.items(): 
            buckets[v_times].append(k_num)


        max_k_buckect = []
        i = -1
        while len(max_k_buckect) < k:
            for num in buckets[i]:
                max_k_buckect.append(num)
                if len(max_k_buckect) == k:
                    return max_k_buckect
            i -= 1




            