1. Share questions you would ask to help understand the question:
- Can there be no anagrams at all, in which each str in strs would be grouped individually in the result?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- hash map (Likely)
- Two pointers (Unlikely)

3. Write out in plain English what you want to do:
- From looking at the questions, the resulting output list can have a length that matches the strs list, if every str is a unique anagram
- What I am thinking, is that, since strs is guarenteed to have at least one str, that str can be appended to the output list
- Then, iterate through the rest of the strs list:
    - iterate through the output list and only check the first str in each List 
    - compare the current str from the strs list to the current str in the output list:
        - if they are anagrams, found through the use of a hashmap to compared character counts:
            - append the str to the current list in the output
        - else
            - append the str to a new list that then gets added to the output
- return the output

4. Translate each sub-problem into pseudocode:
- Initialize a output List[List[str]] to 
- append the first str in strs to a new list. And append that to the output list
- Iterate through the strs list, starting from index 1 (i string): 
    - enter another loop that iterates through the lists in output list:
        - grab the first string (1st)
        - compare the lengths between the two strings
            - if not equal: 
                - break
        - initialize a hashmap 
        - iterate through the 1st string, setting characters with values of 0 in the hashmap if it is not in the hashmap
            - increment that value
        - do the same for the i string (decrementing this time), except, if character is not in the hash map: do this:
            - break
        - iterate through the values in the map
            - if there is a value that is not 0, do this:
                - break
        - if after that, it still continues, than it is an anagram
            - Then, append the i string to the list that the 1st string is in
            - continue
    - if break happened: append i string to a new list, and append that list to the output list
- return the output list

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output: List[List[str]] = []
        output.append([strs[0]])
        for i in range(1, len(strs)):
            currStr = strs[i]
            found = 0
            for strList in output:
                firstStr = strList[0]
                if len(firstStr) != len(currStr):
                    continue
                hashmap = {}
                temp = 0
                for char in firstStr:
                    if char not in hashmap:
                        hashmap[char] = 0
                    hashmap[char] += 1
                for char in currStr:
                    if char not in hashmap:
                        temp = 1
                        break
                    hashmap[char] -= 1
                if temp == 1: 
                    continue
                for value in hashmap.values():
                    if value != 0: 
                        temp = 1
                        break
                if temp == 1: 
                    continue
                strList.append(currStr)    
                found = 1
                break
            if found != 1:
                output.append([currStr])

        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it is it does not use extra libraries or functions
- One weak area is that it is very inefficient. An extermely more efficient route would have been to utilize the sorted method