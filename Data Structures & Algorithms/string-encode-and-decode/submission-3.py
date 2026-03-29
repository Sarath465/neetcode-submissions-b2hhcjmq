class Solution:

    def encode(self, strs: List[str]) -> str:
        l = []
        for i in strs:
            l.append("".join([str(len(i)), '#', i]))
           
        l = "".join(l)
        print(l)
        return l
    def decode(self, s: str) -> List[str]:
        output = []
        if s:
            i=0
            while (i < len(s)):
                length = s.find("#", int(i))
                print(length)
                print(i, s[i:length])
                k = int(s[i:length])
                output.append(s[length+1:length+k+1])     
                print(i, k, output)
                i = length+k+1
            
            
        return output

