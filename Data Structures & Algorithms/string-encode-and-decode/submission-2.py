class Solution:

    # ["this", "is", "my", "name"] -> 4#this2#is
    def encode(self, strs: List[str]) -> str:
        resp = ""
        for st in strs:
            resp += str(len(st)) + "#" + st
        return resp


    # 4#this12#isadfasdfasdfsdf#1a
    def decode(self, s: str) -> List[str]:
        resp = []

        # i = 0, length=""
        # i = 1, length=""
        i = 0
        while(i < len(s)):
            length = ""
            while (s[i] != "#"):
                length += s[i]
                i += 1
            else:
                i += 1
                string = s[i: i + int(length)]
                resp.append(string)
                i += int(length)
        return resp
