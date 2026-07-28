class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set()
        long = 0

        for i in nums:
            cons.add(i)

        for val in cons:
            num = val - 1
            length = 1
            if num in cons:
                continue # NOT THE START OF SEQ
            else:
                num = val + 1
                while True:
                    if num in cons:
                        length += 1
                        num += 1
                    else:
                        long = max(long, length)
                        break

        return long