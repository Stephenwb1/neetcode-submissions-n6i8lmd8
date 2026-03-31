class Solution:

    def encode(self, strs: List[str]) -> str:
        #each word will begin with a number represnting the length of it
        #and a pound sign

        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        #we need to read the length, and once we get to the pound
        #sign we read the string

        result = []

        i = 0

        while i < len(s):
            j = i
            length = ""
            #j and i are at the beginning
            while s[j] != "#":
                length += s[j]
                j += 1
            length = int(length)
            #j is pointing at the pound sign
            i = j + 1
            #i is pointing at the start of the word
            j = i + length
            #j is pointing at the end of the word
            result.append(s[i:j])
            i = j
        return result






