class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # 先比較第一位再去比較該行 
        # for lis in matrix:
        #     if target == lis[-1]:
        #         return True
        #     if target < lis[-1]:
        #         for num in lis:
        #             if target == num:
        #                 return True
        # return False 
        # => runtime: O(m * n) 會爆掉 => 改成 二元搜索
        l1 = 0
        r1 = len(matrix)
        while r1 > l1:
            mid = (l1 + r1) // 2
            if target == matrix[mid][-1]:
                return True
            elif target > matrix[mid][-1]:
                l1 = mid + 1
            elif target < matrix[mid][-1]:
                r1 = mid 

        if l1 >= len(matrix):
            return False  

        l2, r2 = 0, len(matrix[l1])
        while r2 > l2:
            mid2 = (l2 + r2) // 2
            if target == matrix[l1][mid2]:
                return True
            elif target > matrix[l1][mid2]:
                l2 = mid2 + 1
            elif target < matrix[l1][mid2]:
                r2 = mid2 
        return False


