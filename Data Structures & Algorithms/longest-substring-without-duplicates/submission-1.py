class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        elements = set()


        for right in range(len(s)):

            if s[right] not in elements: # DNE in set
                elements.add(s[right]) # Add to set
                maxLen = max(len(elements), maxLen)
                print(maxLen)
            else: # Exists in set
                while s[right] in elements:
                    elements.remove(s[left])
                    left += 1
                elements.add(s[right])


        return maxLen