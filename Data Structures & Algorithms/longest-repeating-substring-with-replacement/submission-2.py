class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 雙迴圈 => Time Limit Exceeded
        # 快慢指標 fast只向右=> O(N)
        hashmap = {}
        slow = 0
        max_length = 0

        for fast in range(len(s)):
            hashmap[s[fast]] = hashmap.get(s[fast], 0) + 1
            is_valid, current_len = self.Isvalid(hashmap, k)
            while not is_valid:
                hashmap[s[slow]] -= 1
                if hashmap[s[slow]] == 0:
                    del hashmap[s[slow]]  
                slow += 1
                is_valid, current_len = self.Isvalid(hashmap, k)
            max_length = max(max_length, current_len)

        return max_length
    def Isvalid(self, hashmap: dict, k: int) -> tuple[bool, int]:
        if not hashmap:
            return True, 0
        total_count = sum(hashmap.values())  
        max_freq_num = max(hashmap.values())  
        is_legal = (total_count - max_freq_num) <= k

        return is_legal, total_count

        