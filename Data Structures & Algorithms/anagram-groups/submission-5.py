class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each and sort all - mn log m 
        # map each str -> check in map and append to list -> return map values - m*n
        map = defaultdict()

        for i in range(len(strs)):
            mapLst = tuple(self.mapString(strs[i]))

            if mapLst not in map:
                map[mapLst] = [strs[i]]
            else:
                map[mapLst].append(strs[i])
        return list(map.values())


    def mapString(self, string):
        strList = [0] * 26
        for i in range(len(string)):
            index = ord(string[i]) - ord('a')
            strList[index] = strList[index] + 1
        return strList