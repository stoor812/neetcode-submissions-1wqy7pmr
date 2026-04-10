class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        k = len(s1)
        hashS1 = {}
        hashS2 = {}

        if len(s1) > len(s2): return False
        
        # Add S1 to hash
        for i in s1:
            if i not in hashS1:
                hashS1[i] = 1
            else:
                hashS1[i] += 1
        
        for right in range(len(s2)):
            window = (right - left) + 1
            x = s2[right]
            y = s2[left]

            if window < k: # Window Too Small
                hashS2[x] = hashS2.get(x, 0) + 1
            elif window == k:
                hashS2[x] = hashS2.get(x, 0) + 1
                if hashS1 == hashS2: return True
            else: # Window Too Big
                hashS2[x] = hashS2.get(x, 0) + 1
                hashS2[y] -= 1
                left += 1
                if hashS2[y] == 0: del hashS2[y]
                if hashS1 == hashS2: return True
        
        return False

 

