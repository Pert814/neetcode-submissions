class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 1 => 1
        n = 2 => 2
        n = 3 => 1 + 2 = 3
        n = 4 => 1 + 3 + 1 = 5
        n = 5 => 1 + 4 + 3 = 8
        ...
        f(n) = f(n-1) + f(n-2)
        '''
        fn = [1,2]
        if len(fn) >= n:
            return fn[n-1]

        while n > len(fn):
            fn.append(fn[-1]+fn[-2])

        return fn[-1] 

