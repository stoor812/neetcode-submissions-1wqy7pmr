class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for word in strs: # Loop through each word in List
            count = [0] * 26 
            for s in word: # Loop through each char in Word
                index = ord(s) - ord('a')
                count[index] += 1
            # Create Key & Add to HashMap
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = [word]
            else:
                hashmap[key].append(word)

        return list(hashmap.values())
        

