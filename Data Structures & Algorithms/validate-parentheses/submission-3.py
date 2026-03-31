class Solution:
    def isValid(self, s: str) -> bool:
        
        par_map = {"}": "{", "]": "[", ")": "("}
        stack = []

        for i in s:
            #  }
            if stack and i in par_map:
                if stack.pop() == par_map[i]:
                    continue
                else:
                    return False
            # ([{
            stack.append(i)
        return len(stack) == 0