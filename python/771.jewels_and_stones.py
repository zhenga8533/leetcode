class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        gems = set()
        for jewel in jewels:
            gems.add(jewel)
        
        count = 0
        for stone in stones:
            if stone in gems:
                count += 1
            
        return count
        
