class Solution:
    def reverseBits(self, n: int) -> int:
        # 使用位元子運算 
        # n //= 2 => n >> 1
        # n % 2 == 1 => (n & 1)
        Output = 0
        for i in range(0,32):
            if (n & 1):
                Output += 2 ** (31-i)
            n >>= 1
        return  Output