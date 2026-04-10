class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            print(mid)
            if nums[mid] == target: return mid

            # CASE 1 - Left Sorted Portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    # Search Right - Target Greater than Middle
                    left = mid + 1
               # elif target < nums[left]:
                    # Search Right - Target Less than leftmost
                #    left = mid + 1 
                else:
                    right = mid - 1

            #CASE 2 - Right Sorted Portion
            elif nums[right] >= nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    # Search Right - mid < target <= right
                    left = mid + 1
                else:
                    right = mid - 1
        
        # TARGET NOT FOUND
        return -1



            
            
            





            
            

        