class Solution:

    #each string begins with the length of it followed by delimiter #

    def encode(self, strs: List[str]) -> str:

        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result


    def decode(self, s: str) -> List[str]:
        #we need to read the length, move over one more character, and then read the string

        result = []

        i = 0 #pointer that we'll use to indicate the start

        while i < len(s):
            j = i
            length = ""
            print("got here")
            while s[j] != "#":
                print(s[j])
                length += s[j]
                j += 1 #increment j until we get to the pound sign
            #i is pointing at s[0], and j is pointing at the pound sign
            i = j + 1 # i is now pointing one char past the delimiter
            j = i + int(length) #j is now pointing at the end of the string we want
            result.append(s[i:j])
            i = j
        return result
