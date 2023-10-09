class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int

        Runtime: 30 ms (Beats 88.14%)
        Memory: 13.6 MB (Beats 50.85%)
        """

        pos = 1
        c = chars[0]
        count = 1

        while pos < len(chars):
            if chars[pos] == c:
                chars.pop(pos)
                count += 1
            else:
                c = chars[pos]
                if count > 1:
                    cs = list(str(count))
                    chars[pos:pos] = cs
                    pos += 1 + len(cs)
                else:
                    pos += 1
                
                count = 1
        if count > 1:
            cs = list(str(count))
            chars[pos:pos] = cs
            pos += 1 + len(cs)
        
        return len(chars)
        
