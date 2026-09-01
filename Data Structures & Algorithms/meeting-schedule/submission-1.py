"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, c: List[Interval]) -> bool:
        # bucket解法 => 無法確認是否可以是小數 且上限是1000000
        # 雙迴圈暴力解 => O(n2)
        # 先排序再回圈 => O(nlogn)

        #以 lambda x: x.start 回傳值為依據排列intervals
        c.sort(key=lambda x: x.start) 
        # lambda x: x.start == 輸入x 回傳 x.start

        for i in range(0, len(c)-1):
            if c[i].end > c[i + 1].start:
                return False
        return True

