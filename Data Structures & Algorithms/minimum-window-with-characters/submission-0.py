class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        shortSub = ""
        hashS = {}
        hashT = {}

        # ADD T TO HASH
        for i in t:
            hashT[i] = hashT.get(i, 0) + 1
        
        # SLIDING WINDOW
        while right < len(s):
            key = s[right]
            #CHECK IF EXISTS IN T
            if s[right] in hashT: 
                hashS[key] = hashS.get(key, 0) + 1

                match = all (hashS.get(char,0) >= hashT[char] for char in hashT)
                
                # COMPARE HASH MAPS
                while match:
                    # REPLACE SUB
                    curr = s[left:right + 1]
                    if shortSub == "" or len(curr) < len(shortSub):
                        shortSub = curr
                    # DECREMENT HASH S 
                    if s[left] in hashS:
                        hashS[s[left]] -= 1
                    left += 1
                    match = all (hashS.get(char,0) >= hashT[char] for char in hashT)
                
                right += 1
            # INCREASE WINDOW
            else: 
                right += 1
        
        return shortSub