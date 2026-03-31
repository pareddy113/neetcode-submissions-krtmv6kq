class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = defaultdict(list)
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            self.dict[word].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        print(self.dict)
        word1_idx = self.dict[word1]
        word2_idx = self.dict[word2]
        print(word1_idx, word2_idx)
        # [1] [2]
        # [8, 9] [2]
        # [1, 5, 9] [3, 10]
        i,j = 0, 0 
        min_dist = float('inf')
        while i < len(word1_idx) and j < len(word2_idx):
            print(i,j)
            if word1_idx[i] < word2_idx[j]:
                min_dist = min(min_dist, abs(word1_idx[i] - word2_idx[j]))
                i += 1
            else:
                min_dist = min(min_dist, abs(word1_idx[i] - word2_idx[j]))
                j += 1
        return min_dist
        

# word: SortedList(1,2)
# practice: [0]
# makes: [1,4]
# perfect:[2]
# coding:[3]

# 3 - 0 = 3, 3 - 4

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)