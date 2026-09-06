class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 補償hashmap => O(N)會爆掉 => 做一個補償數去跑 O(N)
        # 雙迴圈 O(NlogN) => ascending => 雙指標去跑 O(N)
        l = 0 
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: 
                r -= 1 
        return "You lied."
