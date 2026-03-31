class Solution:

    #encode the strings
    #each string begins with len(str)#


    def encode(self, strs: List[str]) -> str:
        
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        #we are going to read the string for the number that represents the length, then once we get to #, start reading the string

        i = 0

        result = []

        while i < len(s):
            j = i
            length_str = ""
            #while not delimiter character
            #   store length of string in variable
            #for length of string
            #   string += characters
            #list.append(string)
            while s[j] != '#':
                length_str += s[j]
                j += 1
           
            length = int(length_str) #the length of the string
            
            #j is pointing at the pound sign
            i = j + 1 #beginning index of word to copy
            j = i + length #end index of word to copy
            result.append(s[i:j])
            #j is pointing at the last character in that string
            i = j
            #next iteration, we start at the next number
        return result