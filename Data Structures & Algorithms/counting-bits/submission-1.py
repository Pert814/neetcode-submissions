class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n) => 前面的補後面的 
        # => Output[i] = Output[i >> 1] + (i & 1)
        # 找 Output[6] 1 1 0 從 Output[3] 找 1 1
        
        # >> 二進位右移: 
        # 4 >> 1 => 1 0 0 => 1 0 => 2
        # 5 >> 2 ==> 1 0 1 => 1 ==> 1

        # & AND 運算子(Int):  
        # 4 & 5 => 1 0 0 & 1 0 1 => 1 0 0 => 4
        # 任意int: i & 1 => .... 1or0 & 0 0 0 ,,,, 1 => 1or0
        
        Output = [0] * (n + 1)

        for i in range(1, n + 1):
            # Output[i] = Output[i >> 1] + (1 if i % 2 == 1 else 0)
            Output[i] = Output[i >> 1] + (i & 1)
        return Output