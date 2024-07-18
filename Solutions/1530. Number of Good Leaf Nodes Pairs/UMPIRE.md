1. Share questions you would ask to help understand the question:
- Am I allowed to use additional data structures?
- Will the nodes have unique values?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Graphs (Likely)

3. Write out in plain English what you want to do: 
- What I am thinking of is breaking down this problem into 2 seperate ones:
    - One for getting all of the node paths 
        - Starting from the root, traverse through the tree and build a path until a leaf node is reached 
    - One for determing the distances between those paths
        - With the paths obtained, compare them from left to right
        - Create a currDistance variable that counts up until the same node is found while the currDistance is less than distance

4. Translate each sub-problem into pseudocode:
- Initialize a list: nodePaths that will hold the paths to the leaves
- create a helper function that takes in a root node and a list as a current path:
    - append the current root to the path
    - if the root is a leaf:
        - append the path to nodePaths
    - if root.left exists:
        - call helper(root.left, current path)
    - if root.right exists:
        - call helper(root.right, current path)
- Initialize an output variable to 0 which will be what is returned 
- call helper(root, [])
- Create a for loop that iterates through nodePaths
    - set a currPath from nodePaths[i]
    - Create a while loop that iterates through the rest of the paths that goes from left -> right:
        - set a comparePath to this path
        - set a currDistance variable to 0 
        - create two pointers that will iterate through the paths
        - create a while loop that iterates through the paths with the pointers
            - compare the values in the paths and only stop when a match is found. Otherwise, move the pointers and increment the currDistance variable
        - if currDistance is less than or equal to distance:
            - increment the output variable
        - repeat the loop with the next path
- return the output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        nodePaths: list[int] = []
        def getNodePaths(root: TreeNode, currPath: list[TreeNode]):
            currPath = currPath + [root]
            if not root.left and not root.right:
                nodePaths.append(currPath)
                return
            if root.left:
                getNodePaths(root.left, currPath)
            if root.right:
                getNodePaths(root.right, currPath) 

        output = 0
        getNodePaths(root, [])

        for i in range(len(nodePaths) - 1):
            j = i + 1
            currPath = nodePaths[i]
            while j < len(nodePaths):
                comparePath = nodePaths[j]
                currDistance = 0
                p1 = len(currPath) - 1
                p2 = len(comparePath) -1
                while p1 != 0 and p2 != 0:
                    if p1 > p2:
                        p1 -= 1
                        currDistance += 1
                        continue
                    if p2 > p1:
                        p2 -= 1
                        currDistance += 1
                        continue
                    if currPath[p1] == comparePath[p2]:
                        break 
                    if p1 != 0:
                        p1 -= 1
                        currDistance += 1
                    if p2 != 0:
                        p2 -= 1
                        currDistance += 1    
                    if currDistance > distance:
                        break
                if currDistance > distance:
                    j += 1
                    continue
                else:
                    output += 1
                    j+= 1
        return output  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this is likely one of the simpliest solutions to follow through as it breaks down the initial problem into 2 more digestible ones
- One weak area is that becuase of its simpliciest, it ends up resulting in poor efficiency
    - To go into more detail: this algorithm is poor in time and space complexity
    - For time, I suspect that it has to do with the fact that while the tree is only travsersed through once, there is then an additional set of computations to go through those constructued paths
    - As for space, I truly believe that it has to do with the fact that the paths are storing the nodes themselves. When initially doing this problem, I was going with the idea that the values of the nodes would be enough. However when that failed, I realized that there are nodes with duplicate values which can mess up the second part of the algorithm. To resolve this, I changed /* currPath = currPath + [root.val] */ to /* currPath = currPath + [root] */
        - Housing such large nodes would definetly take up a lot of space
- I am proud that I was able to come with a solution, but there are definetly a lot of things I would change. 
    - Instead of housing the paths, I document their depths. Then something like LCA could occur where the leaves are checked to see if their distance based on depths is less than distance
- Another approach could be what LeetCoded' editorial was about, and that is to try a graph approach
- There are a lot of more efficient approaches that I will try to breakdown and learn from