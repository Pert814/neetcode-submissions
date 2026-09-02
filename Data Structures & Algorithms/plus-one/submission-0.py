class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        # 切片不會跟著變動 for num in digits[::-1]:時已經做一個digits副本，不會跟著digits變化
        # for num in digits[::-1]:
        #     if num == 9:
        #         digits[i] = 0
        #         if i > i_min:
        #             digits[i-1] += 1
        #         else:
        #             digits = [1] + digits
        #         i -= 1
        #     else:
        #         break

        # 改用 索引值
        digits[-1] += 1
        print(digits)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10 and i == 0:
                digits[i] -=10
                digits = [1] + digits
                print(digits)
            elif digits[i] == 10:
                digits[i] -=10
                digits[i-1] += 1
                print(digits)
            else:
                print(digits)
                break


        return digits

