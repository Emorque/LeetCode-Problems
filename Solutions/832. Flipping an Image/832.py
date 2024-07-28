from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if len(image) == 1:
            image[0][0] = 0 if image[0][0] == 1 else 1
            return image
            
        for i in range(len(image)):
            p1 = 0
            p2 = len(image[i]) -1
            while p1 < p2:
                image[i][p1], image[i][p2] = image[i][p2], image[i][p1] 
                image[i][p1] = 0 if image[i][p1] == 1 else 1
                image[i][p2] = 0 if image[i][p2] == 1 else 1 
                p1 += 1
                p2 -= 1
                if p1 == p2:
                    image[i][p1] = 0 if image[i][p1] == 1 else 1
                    break
        return image