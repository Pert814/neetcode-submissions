class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums裡會少一個數字 =>先求和完整的數列 再扣掉全部的元素
        n = len(nums) + 1
        expected_sum = (0 + n - 1) * n // 2
        for num in nums:
            expected_sum -= num
        return expected_sum
