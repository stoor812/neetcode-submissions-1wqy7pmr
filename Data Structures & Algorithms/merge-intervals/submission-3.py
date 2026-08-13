class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        noInt: List[List[int]] = []
        
        # SORT INTERVALS
        intervals.sort(key=lambda x: x[0])

        curr = intervals[0]
        # MERGE OVERLAPS
        for i in intervals:
            if curr[1] >= i[0]: # EXTEND INTERVAL
                curr[1] = max(curr[1], i[1])
            else:
                noInt.append(curr)
                curr = i
        noInt.append(curr)

        return noInt