class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dMap = set()
        for i in nums:
            if i in dMap: 
                return True
            else:
                dMap.add(i)

        return False

        