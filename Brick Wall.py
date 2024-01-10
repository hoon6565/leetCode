class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:       
        dic = {}
        for row in wall:
            sum = 0
            for i in range(0, len(row) - 1):
                sum += row[i]
                if sum in dic.keys():
                    dic[sum] += 1
                else:
                    dic[sum] = 1
        maxVal = 0
        for i in dic.values():
            maxVal = max(i,maxVal)
        minCross = len(wall) - maxVal
        return minCross