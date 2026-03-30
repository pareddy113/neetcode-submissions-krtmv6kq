class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            elif (len(stack) != 0 and Map[c] == stack.pop()):
                continue
            else:
                return False
        return not stack


        