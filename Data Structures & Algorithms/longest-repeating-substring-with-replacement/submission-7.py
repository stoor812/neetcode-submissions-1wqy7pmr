class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq = {}
        maxFreq = 0
        maxLen = 0

        while right < len(s):
            key = s[right]
            if key not in freq:
                freq[key] = 1
            else:
                freq[key] += 1

            maxFreq = max(maxFreq, freq[key])

            #WINDOW
            if (right - left + 1) - maxFreq <= k:
                maxLen = max(maxLen, right - left + 1)
                print(left, right)
                right += 1
            else:
                freq[s[left]] -= 1 
                left += 1
                right += 1

        return maxLen

            
        