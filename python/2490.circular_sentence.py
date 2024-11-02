class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        words = sentence.split()
        lc = words[0][-1]
        for word in words[1:]:
            rc = word[0]
            if lc != rc:
                return False
            lc = word[-1]

        return True
        
