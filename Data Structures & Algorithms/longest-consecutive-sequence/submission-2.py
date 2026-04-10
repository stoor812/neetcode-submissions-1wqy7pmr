class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        cSet = set()
        Lseq = 1

        # BASE CASE
        if len(nums) == 0: return 0

        # STORE IN SET
        for i in nums:
            cSet.add(i)
        
        # CHECK FOR LONGEST SEQ
        for i in cSet:
            if i - 1 in cSet: #MIDDLE ELEMENT
                continue
            else:
                count = 1
                curr = i
                while curr + 1 in cSet:
                    count += 1
                    curr += 1
                Lseq = max(count, Lseq)

        return Lseq
