class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            wordCount = [0] * 26
            for char in word:
                wordCount[ord(char) - ord('a')] += 1
            wordCountTuple = tuple(wordCount)
            anagramMap[wordCountTuple].append(word)
        return anagramMap.values()