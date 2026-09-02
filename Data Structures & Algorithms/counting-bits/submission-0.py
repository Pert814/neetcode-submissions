class Solution:
    # 暴力解
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += n % 2
            n //= 2
        return cnt

    def countBits(self, n: int) -> List[int]:
        Output = []
        for num in range(n+1):
            Output.append(self.hammingWeight(num))  
        return Output
