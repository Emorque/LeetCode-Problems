1. Share questions you would ask to help understand the question:
- Can there be cases where something like this happens:
  - "abc"
  - "krabifjbc"
  - where characters in s are repeated in the final answer:
    - "abifjbc" (b is repeated twice)

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- hashmap (Likely)
- sliding window (Likely)

3. Write out in plain English what you want to do: 
- So, first things first, iterate through s to get all of the character frequencies
- Then create a sliding window technique that iterates as a for loop from t
  - the window is expanded only until all the characters are covered, likely with a frequency int 
  - once they are all covered, calculate the distance
    - check to see if there are any duplicates with the left most letter, if not, extend right more.
    - if there is, keep moving left until it reaches another character in s
      - recalculate the distance 
  - keep going until both left and right pointer reach the end
- having kept track of the min distance between the pointers for each viable substring,
  - iterate between them to create a string 
- return that string

4. Translate each sub-problem into pseudocode:
- if the length of t is smaller than the length of s, then "" can be returned right away as s cannot contain t as a substring, traversing boolean set to false
- initialize a hashmap, charFreq int (just to find the first viable substring), left and right pointer to 0, minLength int, and pair to indexes starting at (0,0)

- for char in t: 
  - hashmap[char] = 1 + hashmap.get(char, 0)
  - charFreq += 1

<!-- -  in enumerate(s): -->
- while right != len(s):
  - if traversing: 
    - if hashmap[left] < 0:
      - left += 1
      - while s[left] not in hashmap:
        - left += 1
      - if (i - left + 1) < minLength:
        - pair(left, i)
        - minLength = i - left + 1
    else:
      - while s[right] != s[left]:
        - if right == len(s):
          - break
        - right+= 1
        - if s[right] in hashmap:
          - hashmap[s[right]] -= 1
  - else:
    
    - if char in hashmap:
      - if hashmap[s[right]] != 0
        - charFreq -= 1
      - hashmap[s[right]] -= 1
    - if charFreq == 0: *viable substring
      - minLength = min(minLength, i - left + 1)
      - pair = (left, i)
      - traversing = true
  - right += 1

5. Translate the pseudocode into Python and share your final answer:
  <!--  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
