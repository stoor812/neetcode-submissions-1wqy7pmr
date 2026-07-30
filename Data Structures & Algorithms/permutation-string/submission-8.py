class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        hashOne = {}
        hashTwo = {}

        #BASE CASE
        if len(s1) > len(s2): return False

        # HASH S1
        for i in s1:
            if i in hashOne:
                hashOne[i] += 1
            else:
                hashOne[i] = 1
        
        # HASH S2 (FIXED LEN(S1))
        for i in range(len(s1)):
            key = s2[i]
            if key in hashTwo:
                hashTwo[key] += 1
            else:
                hashTwo[key] = 1

        # CHECK INITIAL WINDOW
        if hashOne == hashTwo:
            return True

        # SLIDING WINDOW
        while right < len(s2) - 1:
            keyL = s2[left]
        
            #REMOVE LEFT
            hashTwo[keyL] -= 1
            if hashTwo[keyL] == 0:
                del hashTwo[keyL]

            # SLIDE WINDOW
            left += 1
            right += 1
                
            # ADD RIGHT TO HASH
            if s2[right] in hashTwo:
                hashTwo[s2[right]] += 1
            else:
                hashTwo[s2[right]] = 1
                
            # CHECK WINDOW
            if hashOne == hashTwo:
                return True

        return False

            
