class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        noInt: List[List[int]] = []
        i = 0
        curr = newInterval
        insert = True

        # BASE / EDGE CASE
        if len(intervals) == 0:
            noInt.append(newInterval)
            insert = False
        #if len(newInterval) == 0: return intervals



        while i < len(intervals):
            # INTERVAL IS BEFORE NEW
            if intervals[i][1] < curr[0]:
                noInt.append(intervals[i])
                i += 1

            # INTERVAL IS AFTER NEW
            elif intervals[i][0] > curr[1]:
                if insert:
                    noInt.append(curr)
                    insert = False

                noInt.append(intervals[i])
                curr = intervals[i]
                i += 1

            # INTERVAL OVERLAPS
            elif intervals[i][1] >= curr[0] and insert:
                curr[0] = min(intervals[i][0], curr[0])
                curr[1] = max(intervals[i][1], curr[1])
                while i < len(intervals):
                    if curr[1] >= intervals[i][0]:
                        curr[1] = max(intervals[i][1], curr[1])
                        i += 1
                    else:
                        break
                noInt.append(curr)
                insert = False



        if insert:
            noInt.append(newInterval)



        return noInt
        