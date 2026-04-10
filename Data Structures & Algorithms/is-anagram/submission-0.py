class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        # Length Not Equal
        if len(sorted_s) != len(sorted_t): 
            return False
        else:
        # Length equal compare chars
            for c in range(len(sorted_s)):
                if sorted_s[c] != sorted_t[c]:
                    return False
        return True

        
