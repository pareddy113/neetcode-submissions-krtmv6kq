class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda val: val[0])
        output = [intervals[0]]

        for i in intervals:
            if output[-1][1] < i[0]:
                output.append(i)
                
            else:
                output[-1][1] = max(output[-1][1], i[1])
        return output

        