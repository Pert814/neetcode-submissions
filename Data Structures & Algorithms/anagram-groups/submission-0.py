class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 找重複 => hash map
        # key值？ => 排序後的字
        hashmap = dict()
        for st in  strs:
            # st_sorted = sorted(st)的話 會是List
            # st = str => st_sorted = ["r","s","t"]
            st_sorted = "".join(sorted(st))
            if st_sorted not in hashmap:
                hashmap[st_sorted] = [st]
            else:
                hashmap[st_sorted].append(st)
        # hashmap.values() => dict_values([['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]) 預示圖
        # => 要用list包起來
        return list(hashmap.values()) 
            
