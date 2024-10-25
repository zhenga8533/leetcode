class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]

        for s in folder[1:]:
            last = ans[-1] + '/'

            if not s.startswith(last):
                ans.append(s)
        
        return ans
        
