class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        shots = 1
        last = points[0][1]

        for point in points:
            if point[0] > last:
                shots += 1
                last = point[1]
            else:
                last = min(last, point[1])
        
        return shots
        
