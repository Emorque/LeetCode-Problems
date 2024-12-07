1. Share questions you would ask to help understand the question:
- Can one person trust multiple people?
- What is returned if there are no trust relationships at all?
- Can there be a case where some of the people who are not the judge don't have any trust relationships? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash Map (Likely)
- Set (Unlikely)

3. Write out in plain English what you want to do: 
- Given the definition of a town judge, that means that exactly n-1 people trust them. So in a town of 5 people, 4 people trust this the town judge if they exist
- Else, everyone would have a different number of people who trust them, but never being exactly n-1
- Therefore, a hash map can be made, person: number of people trusting them
- What can be done is that as I iterate through the trust list, increment the value of the person in the map that is trusted; and decrement the value of the person that is trusting (this prevents cases where someone would be declared a town judge (has n-1), but that person trusts someone)
- Then, iterate through the hash map, and if someone is found with a value of n-1, return the person
- If no one is returned, return -1  

4. Translate each sub-problem into pseudocode:
- Initialize a hashMap 
- iterate thorugh trust:
    - if p1 or p2 are not in the hashMap, set them with values of 0
    - do hashMap[p1] -= 1
    - do hashMap[p2] += 1
- iterate through the hashMap
    - if hashmap[person] has value of n-1, return that person
- return -1

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        hashMap = {}
        for p1, p2 in trust:
            if p1 not in hashMap:
                hashMap[p1] = 0
            if p2 not in hashMap:
                hashMap[p2] = 0
            hashMap[p1] -= 1
            hashMap[p2] += 1
        for person in hashMap:
            if hashMap[person] == n - 1: return person
        return -1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it efficiently uses a hashMap 
- One weak area is that a hashMap was used. In this question, a hashMap is added complexity that if would be appropaite it the persons were not ints, but instead strings 
    - Since the person corresponds their value, a list can be used where the index corresponds to the person. For example, index x + 1 represents person x. The same logic can be used.