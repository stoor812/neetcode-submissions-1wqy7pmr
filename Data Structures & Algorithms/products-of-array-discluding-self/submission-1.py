class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [] 
        suffix = [None] * len(nums)
        prod = [None] * len(nums)

        # PREFIX ARRAY
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] * prefix[i - 1])

        # SUFFIX ARRAY
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                print(nums[i])
                print(nums[i + 1])
                suffix[i] = nums[i] * suffix[i + 1]

        #PRODUCT ARRAY
        for i in range(len(nums)):
            if i == 0:
                prod[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                prod[i] = prefix[i - 1]
            else:
                prod[i] = prefix[i - 1] * suffix[i + 1]


        return prod