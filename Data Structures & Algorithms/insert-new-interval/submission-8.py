class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        i = 0
        curr = newInterval

        # BEFORE NEW
        while i < len(intervals) and intervals[i][1] < curr[0]:
            newList.append(intervals[i])
            i += 1
        
        # OVERLAPPING MERGE
        while i < len(intervals) and intervals[i][0] <= curr[1]:
            curr[0] = min(intervals[i][0],curr[0])
            curr[1] = max(intervals[i][1], curr[1])
            i += 1
        
        newList.append(curr)

        # AFTER NEW
        while i < len(intervals):
            newList.append(intervals[i])
            i += 1

        return newList