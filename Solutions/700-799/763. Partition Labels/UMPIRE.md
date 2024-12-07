1. Share questions you would ask to help understand the question:
- So basically, sorting is not an option correct? We can't change the order of the letters in s
- What if there is a letter that is that the start and end of s? Would the answer be the whole string?
- An technically true answer for all of the test cases would just be [len(s)], but what we really want is the smallest possible partitions, in that they cannot be split further?
- Will s have at least one character?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hashmap (Likely)
- Two pointer (Likely)

3. Write out in plain English what you want to do: 
- After realizing that the what we want, are the smallest partitions possible, and s's letters cannot be rearranged, what we we break down the s string with pointers
- Starting from the first letter (1st pointer), set the right most pointer to the last instance of that first letter. Then check if each letter between these two pointers contains all the instances of the letters. So if I have a partition "ab........a", I have to check if all of the letters like b, if all instances of b are in this partition. If not, then I have to move the right pointer further.
- I think this can be done in a while loop that ends once the right pointer reaches the end of s, because 
when that happens, there is no way to split the current partition further
- I think a way to know about this letter instances, is to first go through s with a hashmap to get the character frequencies

4. Translate each sub-problem into pseudocode:
- Initialize a partition count to 0, and an ouput list
- Intitialzie two pointers, both set to 0

- while right != len(s):
  - while hashmap[left] != 0:
    - hashmap[right] -= 1
    - right += 1
    - count += 1
  - while left != right:
    - if hashmap[left] != 0: 
      - break
    - left += 1
  - output.append(count)
  - count = 0

- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left, right = 0, 0
        output = []
        count = 0

        continueRight = False

        charFreq = {}

        for char in s:
            charFreq[char] = 1 + charFreq.get(char, 0)
        
        while right < len(s):
            while charFreq[s[left]] != 0:
                charFreq[s[right]] -= 1
                right += 1
                count += 1
            if right == len(s):
                break
            while left != right:
                if charFreq[s[left]] != 0:
                    continueRight = True
                    break
                left += 1
            if continueRight:
                continueRight = False
                continue
            output.append(count)
            count = 0
        
        output.append(count)

        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that only one pass through the s string is needed with two pointers to build the partitions
- One weak area is that I was able to complete the algorithm using only one additional data strucutre, but because of some the number of variables, it may be confusing to follow why continueRight or that right == len(s) conditionals are present