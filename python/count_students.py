class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        storage = [0, 0]
        for student in students:
            storage[student] += 1
        
        remaining = len(sandwiches)
        for sandwich in sandwiches:
            if storage[sandwich] == 0:
                break
            if remaining == 0:
                break
            storage[sandwich] -= 1
            remaining -= 1

        return remaining
        
