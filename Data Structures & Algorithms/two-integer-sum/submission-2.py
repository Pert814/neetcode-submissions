class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = dict()
        # enumerate => 同時找其索引值跟其值
        for i, i_num in enumerate(nums):
            j_num = target - i_num #要找的值
            if j_num in dict1:
                return [dict1[j_num], i]
            dict1[i_num] = i #沒找到就把值-索引存入dict1
            
            
