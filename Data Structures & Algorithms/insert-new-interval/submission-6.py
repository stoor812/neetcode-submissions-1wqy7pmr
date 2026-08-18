class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        noInt = []
        maxLen = len(intervals)

        # BEFORE NEW-INT
        while i < maxLen and intervals[i][1] < newInterval[0]:
            noInt.append(intervals[i])
            i += 1

        # OVERLAPPING
        while i < maxLen and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        noInt.append(newInterval)

        # AFTER NEW-INT
        while i < maxLen:
            noInt.append(intervals[i])
            i += 1

        return noInt