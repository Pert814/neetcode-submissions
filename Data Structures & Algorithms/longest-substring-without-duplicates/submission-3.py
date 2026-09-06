class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # 找重複的字母 => hashmap {字母: 出現位置}
        # hashmap = dict()
        # max_length = 0
        # Is_duplicate = False
        # for c in range(len(s)):
        #     if s[c] in hashmap:
        #         max_length = max(max_length, c - hashmap[s[c]])
        #         Is_duplicate = True
        #     hashmap[s[c]] = c
        # return max_length if Is_duplicate else len(s)
        # 以重複的字母判斷 substring 但是如果 s = "dvdf" 前面重複會出錯
        # => 再加一個左指標當字串起始位置
        hashmap = dict()
        max_length = 0
        l = -1
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]], l)
            hashmap[s[r]] = r
            max_length = max(max_length, r - l)

        return max_length



        

                
