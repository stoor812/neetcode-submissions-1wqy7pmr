class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mHash = {}
        maxInt = None

        for i in nums:
            # ADD TO HASH
            if i in mHash:
                mHash[i] += 1
            else:
                mHash[i] = 1

            # UPDATE MAX
            if maxInt is None:
                maxInt = i
            elif mHash[maxInt] < mHash[i]:
                maxInt = i

        

        return maxInt
            