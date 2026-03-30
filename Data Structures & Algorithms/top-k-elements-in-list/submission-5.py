class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number in nums
        # Use a dictionary to store the count for each unique number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Step 2: Create a frequency list (buckets)
        # Each index in the list corresponds to the frequency
        # freq[i] contains a list of numbers that appear i times
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Step 3: Collect the top k frequent elements
        res = []
        # Iterate from the highest frequency to the lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)  # Add the number to the result list
                # Stop when we have collected k elementsx
                if len(res) == k:
                    return res