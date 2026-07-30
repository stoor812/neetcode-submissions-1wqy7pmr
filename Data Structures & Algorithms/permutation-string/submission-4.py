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
        
        # HASH S2
        for i in range(len(s1)):
            key = s2[i]
            if key in hashTwo:
                hashTwo[key] += 1
            else:
                hashTwo[key] = 1

        if hashOne == hashTwo: 
            return True
        else:
            right += 1

        # FIXED SLIDING WINDOW
        while right < len(s2):      
            hashTwo[s2[left]] -= 1
            if hashTwo[s2[left]] == 0:
                del hashTwo[s2[left]]
            
            left += 1


            if s2[right] in hashTwo:
                hashTwo[s2[right]] += 1
            else:
                hashTwo[s2[right]] = 1

            print(hashOne, hashTwo)
 
            if hashOne == hashTwo: 
                return True
            else:
                right += 1



        return False

            
