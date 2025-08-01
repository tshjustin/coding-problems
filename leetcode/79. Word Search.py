class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        what i have in mind: 

        1. first letter marks the starting letter 

        2. from the board, find the possible starting positions, via letter matching 

        3. perfrom a DFS in 4 directions, pick or no pick each time , travering the word

        """
        
        # first_letter = word[0]
        # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # word_len = len(word)

        # row = len(board)
        # col = len(board[0])

        # starting_pos = []

        # for i in range(row): 
        #     for j in range(col): 
        #         if board[i][j] == first_letter: 
        #             starting_pos.append((i, j))
        

        # for start in starting_pos: 

        #    :  # put the directions outside to make things easier for us inside the function call 
        #         if dfs(start[0], start[1], 0)


    

        # def dfs(row, col, idx): 
        #     """
        #     idx => Index to tell which position of the word i am currently looking at 

        #     row => row of the current element we are in 
        #     col => col of the current element we are in 

        #     to code this out, think of the scenario of "A"

        #     what do we need to check for the current:

        #     1. check if the letter are equal ! (including the starting pos)

        #     2. then we recurse and go to the next direction 

        #         a. check if we are in bounds 
        #         b. check that we have not run out of words 
            
        #     now need to find a way to return the solution 
        #     """

        #     # base cases -> that would fail 
        #     if idx == word_len-1 or board[row][col] != word[idx]: 
        #         return False 

        #     # base bases -> that would pass ! 
        #     if idx == word_len-1 and board[row][col] == word[-1]: 
        #         return True 

        #     # our next position to go 
        #     new_row = row + direction[0]
        #     new_col = col + direction[1]

        #     if 0 <= new_row < row and 0 <= new_col < col: 
        #         return dfs(new_row, new_col, idx+1)
        
        ROWS, COLS = len(board), len(board[0])
        word_len = len(word)

        def dfs(r, c, idx, visited):

            # if current dont match 
            if board[r][c] != word[idx]:
                return False

            # if last letter - then we know matches since we got till the end 
            if idx == word_len - 1:
                return True

            # mark the current cell as visited --> word matches so we are here 
            visited.add((r, c))

            # 4 directions 
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS and # \____ check if we are within bounds 
                    0 <= nc < COLS and # /
                    (nr, nc) not in visited and # if the next cell we want to go is visited or not 
                    dfs(nr, nc, idx + 1, visited) # try visiitng it --> note that if true, then taht means we found a match ! 
                ):
                    return True # keep recursing retrun True 

            # now the hard part is understanding this and why is it palced here at this nested level 

            """
            After exhausting all directions , then it would would exit the for (directions) loops, hence 
            remvoe the current visited element from the set --> then go back to the previous step ! 

            """
            visited.remove((r, c))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True

        return False
        