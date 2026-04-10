class Solution:

    def encode(self, strs: List[str]) -> str:
        eString = ""

        for word in strs:
            k = len(word)
            eString += str(k) + '#'
            eString += word
        
        print(eString)
        return eString

    def decode(self, s: str) -> List[str]:
        dList = []
        k = ""
        i = 0

        while i < len(s):
            if s[i] != '#':
                k += s[i]
                i += 1
            else: #Start of Word
                i += 1
                length = int(k)
                newWord = s[i: i + length]
                i += length
                dList.append(newWord)
                k = ""

        return dList
