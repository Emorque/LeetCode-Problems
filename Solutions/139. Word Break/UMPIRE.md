1. Share questions you would ask to help understand the question:
- Can the dictionary be empty?
- Is every character in s in dictonary letters? Uppercase/lowercase?
- Can s be empty?
- Are all of the words in dictionary unique?
- Is it fine if a word from the dictionary doesn't get used?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP (Likely)
- Backtracking (Neutral)

3. Write out in plain English what you want to do: 
- Drawing out a decision tree, one thing that I spotted that is important, is that when I find a matching word to the current index I am at, I may not want to proceed right away
- There is chance that I want to use a word that is shorter in length, because the substring following it does have a matching word, whereas if I skipped looking at dictionary words, I may return False when in actuality, True can be returned
- Therefore, something I can do, is have another list, that mirrors s in length
- If I can find a word in dictionary that matches a substring in s, then I can set the index there in the new list to True
- I keep building up if the previous index was true, if it wasn't then, while the word fits, there is no words that fill for the previous substrings
- In the end, I return the last index in the new list

4. Translate each sub-problem into pseudocode:
- match = [False] * len(s) + 1
- match[len(s)] = True *I thought I could go from left to right, but doing -1 would just do to the last index. So I do have to go from right to left

- for i in range(len(s) - 1, -1 , -1):
    - check each word
        - if the word matches the substring, then set the match index of i to match[i = len(word)]
            - As an example, "abb"
            - the match array looks like : [F, F, F, T]
            - dictionary would be {bb, a}
            - bb matches "bb" at starting index 1, so we check match[i + len(word)] = match[1 + 2] = match[3] = True
                - Now, match[i] = True
- Keep this up till the left character is reached, and return match[0] 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        match = [False] * (len(s) + 1)
        match[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(s) - i >= len(word) and s[i:len(word) + i] == word:
                    match[i] = match[i + len(word)]
                if match[i]:
                    break
        return match[0] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a data structure keeps track of the indexes that have words that do match the substring. So, when it comes to building towards a solution, that can always be referenced
- One weak area is that it is not all that intuitive to go backwards for me. I thought about going from left-to-right, and maybe I can, I'll definetly see if I can use similar logic to slowly build towards a solution