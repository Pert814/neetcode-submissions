class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)
        l = 0
        while r > l:
            m = (r + l) // 2
            print(m)
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1