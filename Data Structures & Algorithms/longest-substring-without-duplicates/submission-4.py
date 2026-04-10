class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in elements:
                elements.remove(s[left])
                left += 1
            elements.add(s[right])
            maxLen = max(maxLen, len(elements))
        
        return maxLen