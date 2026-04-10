class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        sufix = deque()
        products = []

        # Init Prefix Product Array O(n)
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prod = prefix[i - 1] * nums[i]
                prefix.append(prod)

        # Init Suffix Product Array O(n)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                sufix.appendleft(nums[i])
            else:
                prod = sufix[0] * nums[i]
                sufix.appendleft(prod)
            
        for i in range(len(nums)):
            if i == 0: # First Element
                products.append(sufix[i + 1])
            elif i == len(nums) - 1: # Last Element
                products.append(prefix[i - 1])
            else:
                prod = sufix[i + 1] * prefix[i - 1]
                products.append(prod)

        return products