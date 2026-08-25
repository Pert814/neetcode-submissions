class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        if len(s) != len(t):
            return False
        for a in s:
            dict1[a] = dict1.get(a,0) + 1
        for b in t:
            if b not in dict1:
                return False
            elif dict1[b] == 0:
                return False
            else:    
                dict1[b] -= 1
        #前面已經判斷長度一樣了，所以這邊判定成功就決定了        
        return True