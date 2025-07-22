class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """ 
        1. We can identify the same users if one of their email is present inside multiple arrays 

        2. If same name but all the email inside is not inside any other arrays of the samename, then we know that this is another person 

        Note that we can see this as a graph problem, since its intuitive lol 


        ### Pseudo code 
        {name: graph}


        For each pair of email, draw an edge, eventually we get a connected graph for each person. 

        For acc in accounts: 
            for email in emails: 
                draw an edge between the all the other ndoes and the current node 

        But now the problem is that once we create this isolated graph, how do we extract the solution ? 
        We can just perform a simple BFS to get all the nodes --> Returns one connected component 

        Another important thing to note is that we cant have {name: graph}, since name is not unique
        Hence we must have some mapping from email -> name | do this for all the email

        how do we know represent the graph ? --> adjanceny list is simple here 

        Node 1 => [2, 4] => Node one is connected to 2 and 4 {1 :[2, 4]} <==> {email_1: [email_2, email_3...]}


        # Now how do we start the BFS ? 

        Note that we can start the BFS by using the emial_to_name, since they are the nodes 
        then we can just update the visted array easily and avoid those that we have already explored 


        # BFS: 
        queue = q

        q.append(current_node)

        while q: 
            append all the childrens of it 
        """

        # # build the email to name mapping for tagging later on 
        # email_to_name, adj_list, visited = {}, {}, {}

        # for acc in accounts: 
        #     name = acc[0]
        #     for email in acc[1:]:
        #         email_to_name[email] = name
        #         adj_list[email] = [] # build the arrays first 
        #         visited[email] = False # note that we need we need to track what we have visited, unlike trees 

        # # now build the graph componetns 
        # for acc in accounts: 
        #     for i in range(1, len(acc) - 1):
        #         adj_list[acc[i]].append(acc[i+1])
        #         adj_list[acc[i+1]].append(acc[i]) # front and back

        # # after the above operation, we would have isolated graphs! 
        # # now we need to perform BFS on the adj_list 

        # from queue import Queue

        # sol = []

        # for email in email_to_name:
        #     q = Queue()
        #     # if not visited, then we start visiting it!  
        #     if not visited[email]: 
        #         component = set()   # this is to track the group / compoennet of connected emails 
        #         q.put(email)
        #         visited[email] = True

        #         while not q.empty(): 
        #             current_mail = q.get()
        #             component.add(current_mail)

        #             # find all the emails assoicated with the current node 
        #             connected_emails = adj_list[current_mail]
                    
        #             # append all the emails that are connected to the current node to the queue that is to be visited later on ! 
        #             for cm in connected_emails: 
        #                 if not visited[cm]: # check before enqueue
        #                     q.put(cm) 

        #         sol.append([email_to_name[next(iter(component))]] + sorted(component))

        # return sol class Solution:

        """
        in the above code, the graph building logic is wrong

        for i in range(1, len(acc) - 1):
            
        for [a, b, c], a<=>b, b<=>c, but not a<=>c hence wrong.

        """

        email_to_name = {}
        adj_list = {}
        
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            
            # Map each email to name and initialize adjacency list
            for email in emails:
                email_to_name[email] = name
                if email not in adj_list:
                    adj_list[email] = []
            
            # Connect ALL emails within this account to each other
            for i in range(len(emails)):
                for j in range(i + 1, len(emails)):
                    adj_list[emails[i]].append(emails[j])
                    adj_list[emails[j]].append(emails[i])
        
        from collections import deque
        
        visited = set() # an easier way is just to use a set to check 
        result = []
        
        for email in email_to_name:
            if email not in visited:
                # Start BFS for this component
                queue = deque([email])
                component = []
                
                while queue:
                    current_email = queue.popleft()
                    if current_email not in visited:
                        visited.add(current_email)
                        component.append(current_email)
                        
                        # Add unvisited neighbors to queue
                        for neighbor in adj_list[current_email]:
                            if neighbor not in visited:
                                queue.append(neighbor)
                
                # Sort emails and add name at front
                component.sort()
                result.append([email_to_name[email]] + component)
        
        return result