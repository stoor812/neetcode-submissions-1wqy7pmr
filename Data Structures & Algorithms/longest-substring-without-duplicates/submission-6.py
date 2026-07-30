class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        maxLen = 0
        seq = set()

        # BASE CASE
        if len(s) == 0: return maxLen
        
        # ADD First Letter to SET
        seq.add(s[left])
        maxLen = max(maxLen, len(seq))
        
        while right < len(s):

            if s[right] in seq: # EXISTS IN SET
                seq.remove(s[left])
                left += 1
            else:
                seq.add(s[right])
                right += 1
                maxLen = max(maxLen, len(seq))

        return maxLen
