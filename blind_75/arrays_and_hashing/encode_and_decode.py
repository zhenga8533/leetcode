class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '# '
        encoded = strs[0]
        
        for s in strs[1:]:
            encoded += '# ' + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == '# ':
            return []
        return s.split('# ')
