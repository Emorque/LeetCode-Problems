1. Share questions you would ask to help understand the question:
- For count, if 4 points and I am asked count for one point and the four points can form a square, do I return 1? or 4 (the list of points can be rearranged)?
- If I am given a point to count that has duplicate points, do I count those duplicate points in my total count?
- If no squares can be formed, do we return 0?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hashmap

3. Write out in plain English what you want to do: 
- I definetly want a hashmap to hold the number of times a point is added to the data strucutre
- Then I also realized how to use these frequencies, which is that when a square is formed, the number of squares that can be formed can be found by multiplifying the frequencies of all the points together 
- Then a list can be used to store the actual unique points themselves

- Now comes the algorithm of determining if how a square can be formed
- After looking at the distances between a square, I realized that the distance between a point and it's diagonal in a square will have the same difference between their x and y values. So (1,1) and (3,3) can be corners in a square because the difference between their x and y values are 2 
  - Then, comes checking it their corners exist. And since a hashmap was used to get that point frequency, I can just check if those corners are keys in the hashmap
    - So in that previous example, I would bascially check if both (1,3) and (3,1) are in the hashmap, and if they are, that a square can be formed. Then I just multiply by their values in the hashmap

4. Translate each sub-problem into pseudocode:
- Refer to 3

5. Translate the pseudocode into Python and share your final answer:
  <!-- class DetectSquares:

    def __init__(self):
        self.frequency = {}
        self.points = []

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.frequency:
            self.points.append(point)
            self.frequency[(point[0], point[1])] = 0
        self.frequency[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        output = 0
        x, y = point
        for xi, yi in self.points: 
            if abs(x - xi) == abs(y - yi) and (x != xi and y != yi):
                if (x, yi) in self.frequency and (xi, y) in self.frequency:
                    output += 1 * self.frequency[(xi, yi)] * self.frequency[(x, yi)] * self.frequency[(xi, y)]
        return output

    # Your DetectSquares object will be instantiated and called as such:
    # obj = DetectSquares()
    # obj.add(point)
    # param_2 = obj.count(point) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the advantage of having that hashmap is used in count to check if corners are used
- One weak area is that I did not have that ((x != xi and y != yi)) line, in the if condition, and the reason why that is needed, is so that a square of 0 area is checked. I should have read the question more closely and saw that positive area part