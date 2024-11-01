class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] == fancy[-1]:
                count += 1
            else:
                count = 1
            
            if count < 3:
                fancy += s[i]

        return fancy
        
