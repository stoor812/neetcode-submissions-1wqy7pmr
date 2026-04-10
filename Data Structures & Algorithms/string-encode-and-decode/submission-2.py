class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = []

        for i in strs:
            k = len(i)
            encodedString.append(str(k))
            encodedString.append("#")
            encodedString.append(i)

        encoded = "".join(encodedString)
        return encoded

    def decode(self, s: str) -> List[str]:
        decodedString = []

        i = 0
        k = ""
        while i < len(s):
            if s[i] != "#":
                k += s[i]
                i += 1
            elif s[i] == "#":
                count = int(k)
                string = s[i + 1: i + count + 1]
                i += count + 1
                #for x in range(count):
                #    string += s[i]
                #    i += 1
                decodedString.append(string)
                k = ""

        return decodedString
