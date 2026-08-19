class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        # SORT INTERVALS
        intervals.sort(key=lambda x:x[0])

        for i in range(len(intervals) - 1):

            # NEXT INTERVAL VALID
            if intervals[i][1] <= intervals[i + 1][0]:
                continue

            # OVERLAPPING INTERVAL
            if intervals[i][1] > intervals[i + 1][0]:
                # REMOVE i + 1
                if intervals[i][1] < intervals[i + 1][1]:
                    count += 1
                    intervals[i + 1][0] = intervals[i][0]
                    intervals[i + 1][1] = intervals[i][1]
                else:
                    count += 1

        return count