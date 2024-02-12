class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        common = defaultdict(int)
        word = ''

        for c in paragraph:
            if c.isalpha():
                word += c.lower()
            else:
                if len(word) > 0 and word not in ban:
                    common[word] += 1
                word = ''
        common[word] += 1
        
        return max(common, key=lambda k: common[k])
        
