1. Share 2 questions you would ask to help understand the question:
- Can this be done without another data structure?
- What if we use mutiple pointers

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- 2 pointers (Likely)
- Multiple passes (Neutral)

3. Write out in plain English what you want to do: 
- What can be done is that, for every character in s, we set two pointers that continually goes to left and right respectively until either the they hit out of bounds or match with a "c".
- Set the distance to that index in answer
- return answer

4. Translate each sub-problem into pseudocode:
- What can be done is that, for every character in s, we first check if it matches c
- if it does, then make the current index of answer be 0
- else, set two pointers, one to the left and the right.
  - set a while loop that iterates so long as the pointers haven't gone out of bounds.
    - if one of the pointers reaches a "c", break from the loop
    - while iterating, be sure to keep a count that then gets added to answer. count increments every time the pointers move
- return answer

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        for i, char  in enumerate(s):
            if char == c:
                answer.append(0)
            else:
                p1 = p2 = i
                count = 0
                while (p1 != 0 or p2 != len(s) - 1):
                    if p1 != 0:
                        p1 -= 1
                    if p2 != len(s) - 1:
                        p2 += 1
                    count += 1
                    if (s[p1] == c or s[p2] == c):
                        break
                answer.append(count)
        return answer -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm runs through the list in one pass
- Weak areas:
  - because it runs through the list once, it still needs the pointers to run through the list to find a match to "c"
    - as a result, if there is a test case where, for example, the only "c" is at the end of a 10^4 long string, my solution requires that that right pointer is always traversing till it gets to the that one "c"
  - This is where solutions that utilize an initial pass through the list to find the "c"s are more efficient. 