class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        size = len(gas)
        i = 0
        j = 0
        count = 0
        while i < size:
            if count == size*2:
                return -1
            if i == 0:
                tank = gas[j%size]
            if tank - cost[j%size] < 0:
                i = 0
            else:
                i += 1
            tank = tank - cost[j%size] + gas[(j+1)%size]
            j += 1
            count += 1
        return j%size
        