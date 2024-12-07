1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Set
- Two pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The two big things are what determines a happy number and making sure that catch that I am in a loop
- In terms of how a happy number, I think a mixture of // 10 and %10 to grab individual digits should be enough
- However, in terms of catching that I am in a loop, that's important as if I don't have a catch, then my program will just compute forever if there is a cycle
- Just isolating cycle detection, I know I can use two pointers if the problem were a LL problem. I think the logic should apply here.
- I'll create a helper function that calcualtes the happy number of a given number, and have two pointers that start at n
    - Then, while fast doesn't equal 1, I'll call the helper on fast twice, and slow once
- If I exist the loop, then that means no loop exists and I can return True
- If slow and fast ever equal each other, than that means that there is cycle

4. Assess the space/time complexity:
- Space: O(1), since all that is being done is math on int variables, with no recursive stack or extra data structure used
- Time: O(n) in the case the n is the number of getHappy calls that results from n. Since this time grows linearly with the given n, time is O(n). 
- ** Asking GPT, says that time is O(logn) because: "In each call to getHappy, the number n is broken down digit by digit, which takes O(d), where d is the number of digits in n. The number of digits in n is approximately O(log n) (in base 10). So each call to getHappy takes O(log n) time."

5. Optional - Give any ways you would improve your solution: