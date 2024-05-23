class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rise = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                rise[index] = i - index
            stack.append(i)
        
        return rise
        
