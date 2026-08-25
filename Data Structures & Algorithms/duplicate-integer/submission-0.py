class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        List_Appeared = []
        for num in nums:
            if num in List_Appeared:
                return True
            else:
                List_Appeared.append(num)
        return False

        