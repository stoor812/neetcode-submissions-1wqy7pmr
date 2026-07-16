class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}

        # ADD ALL VALUES TO HASH - (VAL, INDEX)
        for i in range(len(nums)):
            nMap[nums[i]] = i

        for i in range(len(nums)):
            value = target - nums[i]
            if value in nMap:
                print(True, value)
                
                if i != nMap.get(value):
                    return [i, nMap.get(value)]
        