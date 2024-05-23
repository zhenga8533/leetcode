class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = [0] * 26
        base = ord("A")
        for task in tasks:
            table[ord(task) - base] += 1
        
        table.sort()
        chunk = table[25] - 1
        count = chunk * n

        for freq in table[:25]:
            count -= min(chunk, freq)

        return len(tasks) + count if count >= 0 else len(tasks)
