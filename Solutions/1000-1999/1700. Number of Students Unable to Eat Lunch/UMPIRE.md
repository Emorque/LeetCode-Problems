1. Share 2 questions you would ask to help understand the question:
- What should happen if, for example there is one circular sandwiches followed be a square sandwich, but all students want a square sandwich?
- Can this be done without an external data structure?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Counter (Likely)
- Queue (Neutral) 
- Two Pointer (Unlikely)

3. Write out in plain English what you want to do: 
- Since the students are in a list and not a queue, we cannot pop from the ends in O(1) time.
- Therefore, we could use counter variables, one for each kind of student.
- Once we have the number of square and circle students, we just go through sandwiches, checking if the current sandwich has a matching student
  - if there is a matching student, decrease the counter
  - if there are no more matching students, exit the loop
- return the sum of the counters 

4. Translate each sub-problem into pseudocode:
- Iterate through the students, incrementing the square and circle counts
- Iterate through the sandwiches
  - if the current sandwich has enough students, decrement the respective counter
  - else, break from the loop
- return the sum of both counters 

5. Translate the pseudocode into Python and share your final answer:
  <!--     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        squares = 0
        circles = 0
        for i in range(len(students)):
            if students[i] == 1:
                squares += 1 
            else:
                circles += 1

        for sandwich in sandwiches:
            if sandwich == 1 and squares > 0:
                squares -= 1
            elif sandwich == 0 and circles > 0:
                circles -= 1
            else:
                break
        
        return squares + circles -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strength area we are in O(n) time complexity as we are just iterating through the lists to check values
- One weak area is that this alogithm seems quite simple. I feel like a better way could be done, by revamping either loops. 
