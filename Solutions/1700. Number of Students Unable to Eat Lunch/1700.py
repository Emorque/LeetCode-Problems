from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
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
        
        return squares + circles