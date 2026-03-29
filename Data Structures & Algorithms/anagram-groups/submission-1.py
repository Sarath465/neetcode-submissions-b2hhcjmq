class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_d = {}
        for i in strs:
            key = [0]*26
            for j in i:
                key[ord(j) - ord('a')] += 1
            output_d[tuple(key)] = output_d.get(tuple(key),[]) + [i]
            print(output_d.keys())
        return output_d.values()

        