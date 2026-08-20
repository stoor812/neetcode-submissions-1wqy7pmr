class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx1 = 0
        idx2 = 0
        maxOne = len(firstList)
        maxTwo = len(secondList)
        isect = []

        while idx1 < maxOne and idx2 < maxTwo:
            start = max(firstList[idx1][0], secondList[idx2][0])
            end = min(firstList[idx1][1], secondList[idx2][1])
            
            # VALID ISECT
            if start <= end:
                isect.append([start, end])
                
            # MOVE POINTER
            if (firstList[idx1][1] <= secondList[idx2][1]):
                idx1 += 1
            else:
                idx2 += 1

        return isect