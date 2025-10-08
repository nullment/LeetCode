from typing import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        list = []
        for i in strs:
            string = ''.join(sorted(i))
            #print(string)

            if string not in hash:
                hash[string] = []
            hash[string].append(i)
        list = hash.values()

        return list
