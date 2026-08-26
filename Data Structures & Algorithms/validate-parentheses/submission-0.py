class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #用list來當作stack
        dict1 = {'(': ')', 
            '{': '}', 
            '[': ']'}
        for a in s:
            if a in dict1:
                stack.append(a)
            elif stack:
                if a != dict1[stack.pop()]:
                    return False 
            else:
                return False 
        return not stack
                
                
