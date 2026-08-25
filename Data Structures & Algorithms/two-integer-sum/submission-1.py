class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for a in nums:
            j = 0
            for b in nums:
                if a + b == target and i != j:
                   return [i,j] 
                j += 1            
            i += 1
        