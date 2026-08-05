class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid

            # LEFT SIDE SORTED
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # SEARCH LEFT
                    right = mid - 1
                else: # SEARCH RIGHT
                    left = mid + 1
            else:
            # RIGHT SIDE SORTED
                if nums[mid] < target <= nums[right]: # SEARCH RIGHT
                    left = mid + 1
                else: # SEARCH LEFT
                    right = mid - 1



        return -1