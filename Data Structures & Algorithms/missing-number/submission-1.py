class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 利用 XOR 兩兩銷毀機制 
        # (0^1^2^...^n) ^ (0^1^2^...^(缺失元素)^..^n) => 缺失元素
        nums += [0]
        xorr = 0
        for i in range(0,len(nums)):
            xorr ^= i^nums[i]
        return xorr

        