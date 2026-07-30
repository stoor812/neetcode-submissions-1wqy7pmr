class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq = {}
        maxFreq = 0
        maxLen = 0

        while right < len(s):
            key = s[right]
            window = right - left + 1

            # ADD CHAR TO HASHMAP
            if key not in freq:
                freq[key] = 1
            else:
                freq[key] += 1
            
            #UPDATE MAX FREQ
            maxFreq = max(maxFreq, freq[key])

            #SLIDING WINDOW
            if window - maxFreq <= k:
                maxLen = max(maxLen, window)
                right += 1
            else:
                freq[s[left]] -= 1 
                left += 1
                right += 1

        return maxLen

            
        