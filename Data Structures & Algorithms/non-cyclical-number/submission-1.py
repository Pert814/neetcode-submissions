class Solution:
    def isHappy(self, n: int) -> bool:
        # 暴力解 => 快慢指標 : 空間：O(log n) => O(1)

        def sum_of_the_squares(n: int) -> int:
            sum1 = 0
            #while n > 0:
            while n:
                sum1 += int((n % 10)**2)
                n //= 10 # //= ： 整除(int) /= ：除法(float)
            return sum1

        slow = n 
        fast = sum_of_the_squares(n)
        while slow != fast:
            slow = sum_of_the_squares(slow)
            fast = sum_of_the_squares(sum_of_the_squares(fast))
        if fast == 1:
            return True
        return False
            


        