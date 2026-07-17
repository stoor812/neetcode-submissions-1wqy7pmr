class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMap = {}
        count = [0] * 26
        anagrams = []

        for string in strs:
            # CREATE TUPLE (KEY)
            for s in string:
                index = ord(s) - ord('a')
                count[index] += 1
            key = tuple(count)
            count = [0] * 26                    # RESET COUNT

            # ADD TO HASH
            if key not in aMap:
                aMap[key] = []
            
            aMap[key].append(string)

        for key in aMap:
            anagrams.append(aMap[key])

        return anagrams