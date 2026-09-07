class MinStack:

    def __init__(self):
        self.stack_list = []
        self.diary = []
        

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        self.diary.append(val if not self.diary else min( self.diary[-1], val)) 


    def pop(self) -> None:
        self.stack_list.pop()
        self.diary.pop()

    def top(self) -> int:
        return self.stack_list[-1]
        

    # 其他都沒什麼難度，問題是這裡要O(1)
    # => 做一個額外的日記 紀錄每一步時的當時最小值
    # stack(先進後出) => 所以每一步的最小值在存入時會被定好
    def getMin(self) -> int:
        return self.diary[-1]
        
