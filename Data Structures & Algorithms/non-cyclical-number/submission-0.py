class Solution:
    def isHappy(self, n: int) -> bool:
        # 迴圈暴力解
        # 找出每一位數的平方 => %10 /10 
        # 找出是否重複 => hash set
        # hash set => key == value 的dict 

        def sum_of_the_squares(n: int) -> int:
            sum1 = 0
            while n > 0:
                sum1 += int((n % 10)**2)
                n //= 10 # //= ： 整除(int) /= ：除法(float)
            return sum1
        
        n_hashset = set()
        while n > 1:
            if n in n_hashset:
                return False
            n_hashset.add(n)
            n = sum_of_the_squares(n)
        return True


        


        