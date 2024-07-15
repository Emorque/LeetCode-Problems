1. Share questions you would ask to help understand the question:
- That's intresting, so the descriptions are not in order? Like how the root of the tree in example 1 is in index 2
- If does say only valid test cases, so no need to worry about nodes with 3 children or nodes with 2 parents correct?
- Are all the values unique?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- HashTable (Likely)
- Array Lookup (Likely)
- Recursion (Unlikely)
  
3. Write out in plain English what you want to do: 
- First, since the descriptions are not ordered, one way to solve this is to use a hash table to store the node and its children 
- Once the hash table is set, go through the children nodes and if a node is not in that collection, then it has to be the root of the tree
- Then, build the binary tree starting from the root and keep going down its children

4. Translate each sub-problem into pseudocode:
- Initialize a hash table {} and a set to hold all the child nodes
- Go through the descriptions
    - if the parent is not in the table:
        - set table[parent] to [None,None]
    - if isLeft is equal to 1:
        - set table[parent][0] to child
    - else:
        - set table[parent][1] to child
    - append the child to the set 
- Iterate through the set with all the parents:
    - if the parent is not in the set, 
        - set a variable root: to this parent
        - break from the loop, the root of the tree has been found

- Create a helper function that will be responsible for building the tree:
    - if the input is None, return 
    - create a Node with the value as the input
    - if the value is in the keys of the table, that means its a parent:
        - set the left child as helper(dict[input][0])
        - set the right child as helper(dict[input][1])
    - return the root 

 I need to track down the root node for the tree. 
    - The root should be the only node that has has no parents, meaning that it would never be in the xth index of the lists: [_, x, _]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = [None, None]
            if isLeft == 1:
                nodes[parent][0] = child
            else:
                nodes[parent][1] = child
            children.add(child)
        
        for parent in nodes.keys():
            if parent not in children:
                rootVal = parent

        def helper(value: int):
            if value == None:
                return
            root = TreeNode(value)
            
            if value in nodes.keys():
                root.left = helper(nodes[value][0])
                root.right = helper(nodes[value][1])
            
            return root

        root = helper(rootVal)
        return root -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm uses the dictonary effectively to build the relationships between the parent and child nodes
- One weak area is the lack of need for a helper function. Since I was building the solution, from descriptions -> node relationships -> tree construction, I didn't realize that I could have built the tree as I was figuring out the relationships between the nodes. Then, I could have reused my parents in nodes.keys() function to get the root and return that. 
    - It also would have removed the need to check if value is in nodes.keys() since I would know that the current node is a parent when building the relationships dict. 