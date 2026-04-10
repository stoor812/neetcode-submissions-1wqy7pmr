class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for n in range(len(nums)):
            hash_map[nums[n]] = n

        for n in range(len(nums)):
            complement = target - nums[n]
            if complement in hash_map:
                if n != hash_map[complement]:
                    return [n, hash_map[complement]]
            