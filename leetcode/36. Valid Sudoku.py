class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ 
        Brute force is to check for everthing 

        1. use a set to check for duplicates 

        2. take note of how we traverse the board, espeically for 3*3 squares 
        """

        row_set, col_set, square_set = set(), set(), set() 

        rows = len(board)
        cols = len(board[0])

        # first we check that each row is valid 
        for row in range(rows):
            for entry in board[row]: 
                if entry in row_set:
                    return False 

                if entry.isdigit():
                    row_set.add(entry)

            row_set = set() 

        # check for the valid cols 
        for col in range(cols): 
            for row in range(rows): 
                entry = board[row][col]

                if entry in col_set:
                    return False 

                if entry.isdigit():
                    col_set.add(entry)

            col_set = set() 

        # check the 3*3 now 
        """
        Need a smart way to check for the grid 

        0 1 2 | 4 5 6 | ... 
        """

        # for that 3*3 grid 
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                # now for the elements inside this grid 
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        val = board[i][j]
                        
                        if val in seen: 
                            return False 

                        if val.isdigit():
                            seen.add(val)
        return True


        