class Solution:
    def climbStairs(self, n: int) -> int:
        #空間優化 List => a,b
        a = 1
        b = 2
        
        if n == 1:
            return a
        elif n == 2:
            return b
        
        while n > 2:
            # c = a + b
            # a = b 
            # b = c
            a, b = b, a+b
            n -= 1
        return b
        