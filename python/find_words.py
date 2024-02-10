class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a','s', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        ]
        ans = []

        def inRow(c: str) -> int:
            for i in range(3):
                if c in keyboard[i]:
                    return i

            return -1


        for word in words:
            i = inRow(word[0].lower())

            for c in word:
                if inRow(c.lower()) != i:
                    break
            else:
                ans.append(word)

        return ans
        
