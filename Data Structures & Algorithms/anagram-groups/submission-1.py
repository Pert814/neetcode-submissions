class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs[i] is made up of lowercase English letters.
        # => 可以用 bucket (O(26)) 當 key
        hashmap = dict()
        for st in strs:
            buckets = [0] * 26
            for c in st:
                buckets[ord(c) - ord("a")] += 1
            # 轉成 tuple 才能作為不可變的 Key
            key = tuple(buckets)
            if key not in hashmap:
                hashmap[key] = [st] 
            else:
                hashmap[key].append(st)
        return list(hashmap.values())
        
