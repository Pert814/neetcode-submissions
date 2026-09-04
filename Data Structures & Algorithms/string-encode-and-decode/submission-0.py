class Solution:
    # strs[i] contains any possible characters out of 256 valid ASCII characters.
    # ASCII碼 前256 <=> Unicode 的前 256 個碼位
    # 加密 Unicode 的前 256 個碼位 => emoji(128000開始)
    # 加密後 要變str 解密再轉回list 需要長度符號判斷字串長度 
    # 另外只有長度符號 可能會跟原本字串裡的數字混在一起 => 再加上分欄符號
    # ["Hello","World"] => 5#Hello5#World => ["Hello","World"]

    def encode(self, strs: List[str]) -> str:
        list1 = []
        for string in strs:
            str1 = chr(128000 + len(string)) + chr(128000 + ord("#")) # 長度不論是個位還是十位都轉成"一個“emoji
            for c in string:
                str1 += chr(128000 + ord(c))
            list1.append(str1)
        print(list1)
        str_encoded = "".join(list1)
        print(str_encoded)
        return str_encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        strs_decoded = []
        while i < len(s):
            length = ord(s[i]) - 128000
            i += 2
            i_next = i + length
            str_decoded = ""
            while i < i_next:
                str_decoded += chr(ord(s[i]) - 128000)
                i += 1
            strs_decoded.append(str_decoded)
        print(strs_decoded)
        return strs_decoded


        
