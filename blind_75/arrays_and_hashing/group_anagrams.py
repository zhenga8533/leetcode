class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            sort = ''.join(sorted(word))
            anagram[sort].append(word)
        
        return list(anagram.values())
        
