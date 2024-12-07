from typing import List
import collections

class Solution:
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
        return output    