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
        length = len(s)

        # Base Case No Strings
        if(length == 0): return decodedString

        i = 0
        k = ""
        number = True
        while i < len(s):
            if number == True and s[i] != "#":
                k += s[i]
                i += 1
            elif number == True and s[i] == "#":
                count = int(k)
                string = ""
                i += 1
                for x in range(count):
                    string += s[i]
                    i += 1
                decodedString.append(string)
                k = ""

        return decodedString
