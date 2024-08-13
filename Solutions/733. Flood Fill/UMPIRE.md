1. Share questions you would ask to help understand the question:
- When filling, could it be that at the starting pixel has no neighboring pixels with the same value. Ex: a pixel with a value of 1 surrounded only by non-1 valued pixels?
- Can the starting color be the same as the desired color?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- For practice, I want to try to use BFS with a queue. 
- Start by appending the current pixel to the queue.
- Then, change the current pixel to the desired color, and then only add the neighboring pixels if they share the same value as the starting pixel (which may need to be initialized as a separate variable)
- Return the image grid

4. Translate each sub-problem into pseudocode:
- Initialize a startColor int to match the value of image[sr][sc]
- Initialize a queue with the starting tuple(sr, sc)
- While the queue is not empty:
    - pop left from the queue 
    - set the value of the image[sr][sc] to color
    - check the neighboring pixels, keeping in mind any border, and if their value matches the startColor, append them to the queue
- Return the image grid 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        queue = deque()
        startColor = image[sr][sc]
        queue.append((sr, sc))

        while queue:
            pixel = queue.popleft()
            row = pixel[0]
            col = pixel[1]
            image[row][col] = color

            if row > 0 and image[row - 1][col] == startColor:
                queue.append((row-1, col))
            if row < len(image) - 1 and image[row + 1][col] == startColor:
                queue.append((row+1, col))

            if col > 0 and image[row][col - 1] == startColor:
                queue.append((row, col - 1))
            if col < len(image[0]) - 1 and image[row][col + 1] == startColor:
                queue.append((row, col + 1))
        return image -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the recursion stack is not used, just the queue data structure
- One weak area that there is a lot going on, from the tuples in the queue to the variables meant to hold information, it can make it hard to read