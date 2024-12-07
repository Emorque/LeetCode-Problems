1. Share questions you would ask to help understand the question:
- If there are no paths, return an empty List?
- Will there be paths that only differ by the last node?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Helper (Likely)
- Recrusion (Likely)
- Level Search (Neutral)
  
3. Write out in plain English what you want to do: 
- Something that I can use is a helper function that builds a string as long as there exists children
    - Then, whenever there is no longer any children, return that string
- Add those strings into the result list and return the list 

4. Translate each sub-problem into pseudocode:
- Base case in the main function that returns an empty result list if there are no nodes at all
- Set up a result list that will hold all the paths
- Set up a helper function that takes in a str and a node:
    - if the root node doesn't exist, append the current str to the result list
    - call helper(root.left, str + "-> root.val") if left exists
    - call helper(root.right, str + "->root.val") if right exists
return the result list

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result : List[str] = []
        if not root:
            return result

        def helper(currNode: Optional[TreeNode], currStr: str):
            if not currNode.left and not currNode.right:
                result.append(currStr+str(currNode.val))
            currStr += str(currNode.val)+"->"
            if currNode.left:
                helper(currNode.left, currStr)
            if currNode.right:
                helper(currNode.right, currStr)

        helper(root, "")
        return result -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it is a simple algorithm to follow. Just iterate through the nodes and build onto a string if that path exists
- One weak area is that this algorithm can be improved on in multiple ways.
    - For example, instead of concatanating strings, list operations can be used to append an inital path and then pop it after exploring the child nodes