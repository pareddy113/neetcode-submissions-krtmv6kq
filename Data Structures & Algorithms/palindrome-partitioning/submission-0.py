class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []


        def palindrome(a):
            l = 0
            r = len(a) - 1
            # abba
            # abcba
            while l < r:
                if a[r] != a[l]:
                    return False
                l += 1
                r -= 1
            return True

        def par(start, currList):
            
            if (start >= len(s)):
                res.append(currList[:])
                return

            # []
            # a a b i=0, j=0,1,2
            # 
            for i in range(start, len(s)):
                if palindrome(s[start:i + 1]):
                    currList.append(s[start:i + 1])
                    par(i + 1, currList)
                    currList.pop()

        par(0, [])
        return res