"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        idxOne = 0
        idxTwo = 0
        count = 0
        maxCount = 0
        
        # SPLIT AND SORT S/E
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        # SWEEP
        while idxOne < len(starts) or idxTwo < len(ends):
            # FILTER STARTS & ENDS
            if idxOne < len(starts) and idxTwo < len(ends):
                if starts[idxOne] < ends[idxTwo]:
                    count += 1
                    maxCount = max(count, maxCount)
                    idxOne += 1
                else:
                    count -= 1
                    idxTwo += 1
            # FILTER ONLY ENDS
            else:
                count -= 1
                idxTwo += 1

        return maxCount
        