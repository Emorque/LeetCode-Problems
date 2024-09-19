1. Share questions you would ask to help understand the question:
- What is the expected range that num1/num2 can represent?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely


3. Write out in plain English what you want to do: 
- As with doing multiplcation by hand, there will be integers that need to be held, moved over, and considered as a carry, so I think a way to simplify this first is to have a array that will just hold these numbers for me
- Then, I just perform traditional multiplication, liking needed a nested for loop and calculting the result digit by digit
- Then at the end, since the array should have the result in reverse order, as it gets converted to a string, I can just set it as a string 

4. Translate each sub-problem into pseudocode:
- The first check is to see if either of the nums are zero, becuase if it is, then "0" can be returned right away 
- initialize an array with 0's as values and with a size of both lengths added
- Then create a loop that iterates from the right to the left of the num1 string
  - Do the same for the num2 string
    - get the current result by multiplying these two digits
    - add answer[i + j] with that result which do the (adding 0 at the right for every 10s digit) 
    - add answer[i + j + 1] with the carry on [i + j] if it has one ([i + j] // 10)
    - set answer[i + j] with %10, since the next element now has the carry
  
- there is chance that there are leading 0s to the right, so just pop them out of the list
- at this point I can reverse the ints in the array, but for simplicity, I'll just convert the array to a string now and use reverse()

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        
        numArray = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                numArray[i + j] += digit
                numArray[i + j + 1] += (numArray[i + j] // 10)
                numArray[i + j] = numArray[i + j] % 10

        while numArray[-1] == 0:
            numArray.pop()

        numArray = numArray[::-1]
        answer = "".join(str(num) for num in numArray)

        return answer  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm makes use of this numArray to hold the carry values and keeping track of what numbers are in each digit
- One weak area is that in order to do this, a lot of reversing in needed