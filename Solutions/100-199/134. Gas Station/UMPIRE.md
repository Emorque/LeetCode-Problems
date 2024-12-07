1. Share questions you would ask to help understand the question:
- Can there be a case where all the gas stations serve less gas than it takes to reach the next station?
- There be negative values?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- 

3. Write out in plain English what you want to do: 
- Going through the examples by hand, I realized a few things:
  - If none of the stations fuel enough gas to reach the next station, then none of them can be a starting point, so -1 should be returned 
  - the starting point should always be the station that has the greatest gas gain (gas fueled - gas needed to travel to next station) and is the one that appears first. If there are two stations that have equal gas gain, then starting at the first one gives a greater chance of completely the full cycle
  - The circuit can be fully traveled if the sum of all gas gains is positive. If it is negative, then at some point, we need more to travel than is possible to obtain

4. Translate each sub-problem into pseudocode:
- Initialize a index int, gasSum int, maxGasGain to 0
- Create a loop that iterates through gas
  - gasGain = (gas[i] - cost[i])
  - if gasGain > maxGasGain:
    - index = i
    - maxGasGain = gasGain
  - gasSum += gasGain

- return index if gasSum >= 0 else -1

<!-- index = 0
        gasSum, maxGasGain = 0, 0

        enoughGas = 0

        for i in range(len(gas)):
            gasGain = gas[i] - cost[i]
            enoughGas += gasGain
            if gasGain > maxGasGain or enoughGas < 0:
                index = i
                maxGasGain = gasGain
                enoughGas = gasGain
            gasSum += gasGain
        
        return index if gasSum >= 0 else -1-->

- This was as far as I got with almost all of the testcases working, but it wouldn't work for test cases like gas: [5,5,1,3,4], cost[[8,1,7,1,1].

- After some more reworking, I think I was almost right. The logic of gasSum >= 0 does work. However, there is something that I did not fully realize till now:
  - from one station to the next, if at any point the gas tank ever reaches below 0, then that station can't be a starting point
  - however, if one station does reach the end of the gas/cost lists, and gasSum >= 0, then it that station can both reach from the current station to the rightmost, and theoretically have enough gas to go from the leftmost station to the current station, thus completely a full cycle


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasSum = 0
        tank = 0
        station = 0

        for i in range(len(gas)):
            gasGain = gas[i] - cost[i]
            tank += gasGain
            if tank < 0:
                station = i + 1
                tank = 0
            gasSum += gasGain
        
        return station if gasSum >= 0 else -1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area of this algorithm is that, thanks to the ideas explained above, only one pass of the gas and costs lists are needed to see if a start station is possible
- One weak area is that I did not explain the logic in any comments, so understanding the if statements and the idea of a non-viable station may not be clear