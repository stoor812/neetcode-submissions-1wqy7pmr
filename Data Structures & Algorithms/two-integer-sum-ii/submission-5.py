class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            a = numbers[left]
            b = numbers[right]
            c = a + b

            if c < target:
                left += 1
            elif c > target:
                right -= 1
            else:
                return [left + 1, right + 1] 