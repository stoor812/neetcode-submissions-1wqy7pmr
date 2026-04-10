class Solution:

    def encode(self, strs: List[str]) -> str:
        eString = ""

        for word in strs:
            k = len(word)
            eString += str(k) + '#'
            eString += word

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
                #i += 1
               # length = int(k)
                newWord = s[i + 1: i + int(k) + 1]
                i += int(k) + 1
                dList.append(newWord)
                k = ""

        return dList
