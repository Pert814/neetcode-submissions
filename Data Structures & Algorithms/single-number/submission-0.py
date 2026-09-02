class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash set => 空間度O(n)會爆掉
        # XOR運算(Booling):^
        # True ^ False => True
        # True ^ True => False
        # XOR運算(Int):^
        # 4^3 => 1 0 0 ^ 0 1 1 => 1 1 1 => 7 
        # 每一個位元當一個開關 遇到同樣數字 => 抵銷
        start = 0 # 全關
        for num in nums: # 開關疊加
            start = start ^ num 
        return start