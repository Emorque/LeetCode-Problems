from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        track = []

        for i in range(len(position)):
            track.append((position[i], (target - position[i]) / speed[i]))
        
        track.sort()

        maxTOA = track[-1][1]
        for i in range(len(track) - 2, -1, -1):
            if track[i][1] > maxTOA:
                maxTOA = track[i][1]
                fleets += 1
        return fleets 