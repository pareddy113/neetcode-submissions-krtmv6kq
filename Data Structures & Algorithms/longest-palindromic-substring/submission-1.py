class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # odd length
        startIndex = 0
        maxLength = 0
        i = 0
        while (i < len(s)):
            l,r = i, i
            while(l >= 0 and r < len(s)):
                if s[l] == s[r]:
                    
                    if (r - l + 1) > maxLength:
                        startIndex = l
                        maxLength = r - l + 1
                        print("index={} {}", startIndex, maxLength)
                    print(str(i) + s[l] + s[r] + str(l) + str(r))
                    l -= 1
                    r += 1

                else:
                    break
            i += 1

        i = 0
        while (i < len(s)):
            l,r = i, i+1
            while(l >= 0 and r < len(s)):
                if s[l] == s[r]:
                    if (r - l + 1) > maxLength:
                        startIndex = l
                        maxLength = r - l + 1
                    
                    l -= 1
                    r += 1
                else:
                    break
            i += 1
        print(l, maxLength)
        return s[startIndex: startIndex+maxLength]
                

        # even length