class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Can perform a DFS - Recursively epxlore all the possible paths from the given cell state 

        Perform the update step as we go along 
        """

        if not image:
            return []

        rows, columns = len(image), len(image[0])
        start_color = image[sr][sc]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        if start_color == color:
            return image

        def dfs(i, j):
            """
            Peform the recursive search and update 
            """
            
            # base case - also note that we perform the update iff the next color to explore is equal to the start colour 
            if i < 0 or i >= rows or j < 0 or j >= columns or image[i][j] != start_color:  # ensure that >= since if i = 10, and limit is 10, then 10+1 > 10
                return 

            # if the same colour, then we perform the update step - In this implementation, the start cell is treated as a start state too 
            image[i][j] = color 

            for direction in directions:
                dfs(i+direction[0], j+direction[1])

        dfs(sr, sc)
        return image  