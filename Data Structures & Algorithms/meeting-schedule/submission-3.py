"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i : i.start)

        if len(intervals) <= 1:
            return True
            
        pre_end = intervals[0].end

        for i in intervals[1:]:
            if pre_end <= i.start:
                pre_end = i.end
            else:
                return False
        return True
