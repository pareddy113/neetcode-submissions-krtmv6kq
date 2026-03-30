class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "$" + string
        return res

    # 2$he10$avinashred
    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) == 0:
            return []

        decodedStrs = []
        index = 0
        strLength = ""
        while (index < len(s)):
            if s[index] == "$":
                length = int(strLength)
                endIndex = index + 1 + length
                decodedStr = s[index + 1: index + 1 + length]
                decodedStrs.append(decodedStr)
                index = endIndex
                strLength = ""
            else:
                strLength += s[index]
                index += 1
        return decodedStrs

        