1. Share questions you would ask to help understand the question:
- Can integers in nums be negative or 0?
- What is the range of length nums can be?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP (Likely)

3. Write out in plain English what you want to do: 
- By drawing a decision tree, I realized that there were subarrays that contained other subarrays
    - In a way, if I continued down this route, I would be doing the same work multiple times
- It is a bit difficult to explain without the drawing, but basically, by going from left to right, and gettign each subarray at that index (this grows to the right till the last index), there were subarrays in index x that were in index x - 1.
- So what if I went in reverse?
- What if I used a stack to store all the products I currently have
- Then, as I go to the left, I popped all the products from the stack, multiply them by my current number, and then push them back onto the stack. With the current number being the last
- Do this each time, bascially building ontop of previous calculations
    - And at the same time, keeping track of a maxProduct

4. Translate each sub-problem into pseudocode:
- Initialize a products queue
- Intiailize a maxProduct

- for i in range(len(nums) - 1, -1, -1):
    - for j in range(len(stack)):
        - product = nums[i] * stack.pop(0)
        - maxProduct = max(maxProduct, product)
        - stack.append(product)
    - stack.append(nums[i])
    - maxProduct = max(maxProduct nums[i])

- return maxProduct

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        products = []
        maxProduct = nums[0]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(products)):
                product = nums[i] * products.pop(0)
                maxProduct = max(maxProduct, product)
                if product not in products or nums[i] == -1:
                    products.append(product)
            products.append(nums[i])
            maxProduct = max(maxProduct, nums[i])
        
        return maxProduct -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that any previous work that was done with a subarray is saved as an int in this stack, which makes calculating new products very quick, as opposed to recalculating entire subarrays each time
- One weak area is that while this is efficient in memorizing all of the products, it is not the most optimal solution. 
    - There is a better solution that uses only two ints to build ontop of, and in doing so, saves the need of this queue data structure and is quite interesting. This more optimized solution is on the py file too. 