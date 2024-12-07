1. Share 2 questions you would ask to help understand the question:
- Could this be done with one run through the array?
- What should be returned for an empty array?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash Map (Likely)
- Set (Neutral)

3. Write out in plain English what you want to do:
- The way I see, we may need to use a hash map
- We iterate through the list, appending new numbers onto the hash map, and increment the value if it exists
- Then, we compare the values in the hash map to see if there are any duplicates
- return false if there are, true otherwise

4. Translate each sub-problem into pseudocode:
- As we iterate through the list, we will append any new numbers to our map with initial values (Key: num, Val: 1)
  - If we come across a number that exists within the map, we increment the 'Val' by 1
- After we have gone through the the list, we then move onto our hash map, checking the values
  - If there are any duplicate 'Vals', then we return False.
  - Else, return true. 

5. Translate the pseudocode into Python and share your final answer:
  <!-- def uniqueOccurrences(arr: List[int]) -> bool:
  hashMap = {}
  for num in arr:
    if num in hashMap:
      hashMap[num] += 1
    else:
      hashMap[num] = 1

  hashSet = set(hashMap.values())
  return len(hashMap.values()) == len(hashSet)-->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strength is that we are only iterating through the list once, and then only grabbing the lengths of the set and map
- One weak area if that, perhaps it could done with less space complexity. 