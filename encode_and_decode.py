from typing import List 

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_parts = []
        for word in strs:
            encoded_parts.append(f"{len(word)}!{word}")
        return ''.join(encoded_parts)
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '!':
                j += 1
            length = int(s[i:j])
            i = j + 1
            decoded_strs.append(s[i:i + length])
            i += length
            
        return decoded_strs
