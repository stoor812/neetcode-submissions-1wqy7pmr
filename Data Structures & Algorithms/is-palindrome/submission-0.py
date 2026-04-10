class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        NS = low.replace(" ", "")

        left = 0
        right = len(NS) - 1

        while left < right:
            if NS[left].isalnum() == False:
                left += 1
            elif NS[right].isalnum() == False:
                right -= 1
            elif NS[left] == NS[right]:
                left += 1
                right -= 1
            else:
                return False

        return True