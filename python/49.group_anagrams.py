class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Runtime: 93 ms (Beats 82.88%)
        # Memory: 19.5 MB (Beats 76.4%)
      
        anagram = defaultdict(list)

        for word in strs:
            sort = ''.join(sorted(word))
            anagram[sort].append(word)
        
        return list(anagram.values())
        
