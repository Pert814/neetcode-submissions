class Solution:
    def reverseBits(self, n: int) -> int:
        Output = 0
        for i in range(0,32):
            if n % 2 == 1:
                Output += 2 ** (31-i)
            n //= 2
        return  Output