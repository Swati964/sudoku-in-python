def find_next_empty(puzzle):
    #find the next  row, col on the puzzle that's not filled yet --> rep with -1
    #return row, col tuple (or B=None,None) if there is none
    #I am using 0-8 for indices

    for r in range(9):
        for c in range(9): #range(9) is
            if puzzle[r][c] ==-1:
                return r, c
    
    return None, None #if no space in the puzzle are empty(-1)

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the roe/col of the puzzle is a valid guess
    #return True if is valid, False otherwise

    #row part:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
        
    #colume part:
    # col_vals = []
    # for i in range(9):
    #     9col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)] 
    if guess in col_vals:
        return False

    #and then the square
    #where 3x3 square start
    #and iterate over the 3 values in the row/column

    row_start = (row // 3) * 3  # 1 // 3 = 0, 5 // 3 = 1, ......
    col_start = (col // 3) * 3

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    #checks pass
    return True

def solve_sudoku(puzzle):
    #solve sudoku by using backtracking 
    #this puzzle is a list of list , where each list is a row in our puzzle
    #return whether a solution exists
    #mutates puzzle to be the solution (if solution exists)

    #step1: choose somewhere on the board/puzzle to make a guess
    row, col = find_next_empty(puzzle) 

    #step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    #step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1,10):  # range is 1,2.....9
        #step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if this is valid, then place that guess on the puzzle!
            puzzle[row][col] = guess
            # recurse using this puzzle!
            # step 4: recursively call our fuction 
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid OR if guess doesnot solve the puzzle
        #backtrack and try a new number
        puzzle[row][col] = -1  #reset the guess

    #step 6: if none of the numbers we tried is not worked, then this puzzle is UNSOLVED!
    return False

if __name__ == '__main__':
    example_board = [
        [3,9,-1, -1,5,-1, -1,-1,-1],
        [-1,-1,-1, 2,-1,-1, -1,-1,5],
        [-1,-1,-1, 7,1,9, -1,8,-1],

        [-1,5,-1, -1,6,8, -1,-1,-1],
        [2,-1,6, -1,-1,3, -1,-1,-1],
        [-1,-1,-1, -1,-1,-1, -1,-1,4],

        [5,-1,-1, -1,-1,-1, -1,-1,-1],
        [6,7,-1, -1,-1,5, -1,-1,-1],
        [1,-1,9, -1,-1,-1, 2,-1,-1],
    ]
    print(solve_sudoku(example_board))
    print(example_board)