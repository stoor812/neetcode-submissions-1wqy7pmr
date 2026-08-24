class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        threeSums = []

        # SORT ARRAY
        nums.sort()

        # TARGET + TWO-POINTER APPROACH
        for i in range(len(nums) - 2):
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if target + nums[left] + nums[right] < 0:
                    left += 1
                elif target + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    triples.add((target, nums[left], nums[right]))
                    left += 1
                    right -= 1

        # ADD TRIPLES TO LIST
        threeSums = [list(t) for t in triples]

        return threeSums