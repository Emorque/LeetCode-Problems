1. Share questions you would ask to help understand the question:
- Are the emails case sensitive?
- Can the sorted method be used?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Graphs (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- A graph can be made from the given list, where the emails are connected by whether they share the same user
- Remembering to account for the first element, these emails will be connected to each other
- Then, traverse through dfs, with a visited set so as to not traverse through already traversed nodes
- For each email in the graph, traverse through the connected emails, setting them to a list that contains the associated name 
- Once each email is traversed, return the final list

4. Translate each sub-problem into pseudocode:
- Initialize a graph with a set
- set up a hash map to keep track of the emails to the name 
- for each account in the accounts list:
    - initialize a name variable with the first element in account ("John")
    - for each email in the account list:
        - connect the email with the name
- Set up an output list to hold the final result
- set up a visited set to not traverse already traversed emails
- for each email in the graph
    - initialize a list to hold the emails
    - initialize a list to hold the final result 
    - if the email is not in the visited set:
        - append the email to the list
        - append the email to the visited set
        - while the email list has elements:
            - pop from the list
            - append the popped email to the final result list
            - for each edge in the graph[popped email]:
                - if the edge(visiting email) is not in visited:
                    - append the edge to the email list
                    - apppend the edge to the visited set
    - append the name + the sorted final result list to the output list


5. Translate the pseudocode into Python and share your final answer:
  <!--  class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        emailToName = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)

                emailToName[email] = name
        
        output = []
        visited = set()

        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)

                emailList = []

                while stack:
                    node = stack.pop()
                    emailList.append(node)

                    for edge in graph[node]:
                        if edge not in visited:
                            stack.append(edge)
                            visited.add(edge)
                output.append([emailToName[email]] + sorted(emailList))
        return output    -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this is an efficient solution, not traversing through already traversed emails
- One weak area is the readability, there are many interacting data structures that it is can be difficult to follow