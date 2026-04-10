class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_Sum = nums[0]
        cur_Sum = nums[0]

        for i in range(1, len(nums)):

            cur_Sum = max(cur_Sum + nums[i], nums[i])
            max_Sum = max(max_Sum, cur_Sum)

            print(cur_Sum)
            print(max_Sum)

        return max_Sum

        