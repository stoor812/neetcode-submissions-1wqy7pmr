class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        maxFreq = 0
        maxLen = 0

        for right in range(len(s)):
            window = (right - left) + 1
            x = s[right]

            # Add Char to Hashmap
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1
            # Check for Highest Frequency
            maxFreq = max(hashmap[x], maxFreq)

            # Shrink Window
            while window - maxFreq > k:
                #Reduce Freq
                hashmap[s[left]] -= 1
                left += 1
                window = (right - left) + 1

            maxLen = max(maxLen, window)

        return maxLen
