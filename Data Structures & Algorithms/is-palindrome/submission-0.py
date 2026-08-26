class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower().replace(" ", "")
        string1 = ""
        string2 = ""
        for a in string:
            if a.isalnum():
                string1 += a
                string2 = a + string2
        print(string, string2)
        if string1 == string2:
            return True
        return False 
