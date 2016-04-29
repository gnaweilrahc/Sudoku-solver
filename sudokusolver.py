from numpy import zeros, copy, array

class SudokuSolver(object):
    """
    SudokuSolver(object, imethod="userinput")

    A class to solve sudokus.

    Parameters
    ----------
    imethod : input-method, optional
        The desired input method for the Sudoku. Available options with their
        imethod codes are:
        No input: None         (NB: an input can be added later)
        User input: 'userinput'
        Import from text file: 'imptfrmtxt'
        Alternatively, the sudoku array can be input directly
    """
    def __init__(self, input_method = None):
        """
        This class controls the inputs of the sudoku.

        Constructor: SudokuSolver(sudoku)
        """
        self._original_sudoku = zeros((9,9),dtype=int)
        if input_method == None:
            pass
        elif input_method == "userinput":
            self.input_sudoku()
        elif input_method == "imptfrmtxt":
            self.import_from_text_file()
        else:
            self._original_sudoku = input_method
        self._sudoku = copy(self._original_sudoku)

        self._poss = {}
        for a in range(0,9):
            for b in range(0,9):
                self._poss[(a,b)] = [n for n in range(1,10)]
        self._changes_made = True

    def input_sudoku(self):
        """
        Gives the user a prompt to input the sudoku.

        input_sudoku() -> None
        """
        print("Input Sudoku:")
        for a,row in enumerate(self._original_sudoku):
            self._original_sudoku[a] = [int(i) for i in input("Row {0} (using \
' ' as separators):\n".format(a+1)).strip().split()]

    def import_from_text_file(self):
        """
        Imports a Sudoku from a text file.

        import_from_text() -> None
        """
        open(input("Import file location: "))
        pass

    def print_sudoku(self):
        """
        Prints the sudoku to the console.

        print_sudoku() -> None
        """
        print(self._sudoku)

    def print_original_sudoku(self):
        """
        Prints the starting sudoku puzzle to the console.

        print_original_sudoku() -> None
        """
        print(self._original_sudoku)

    def get_row(self,a):
        """
        Returns the row of the sudoku for the point a.

        get_row(int, int) -> [int]
        """
        return self._sudoku[a]

    def get_col(self,b):
        """
        Returns the column of the sudoku for the point b.

        get_col(int) -> [int]
        """
        return [i[b] for i in self._sudoku]

    def get_squ_index(self,c):
        """
        Returns the index of the sub-square of the sudoku for point c where
        point c is given by the index (a,b).

        get_squ_index(int,int) -> (int,int)
        """
        (a,b) = c
        return(a//3,b//3)

    def get_squ(self,z):
        """
        Returns the sub-square values of the sudoku for the given sub-square z,
        given by the sub-square index (x,y).

        get_squ((int,int)) -> [[int]]
        """
        (x,y) = z
        return [vals[3*y:3*y+3] for vals in self._sudoku[3*x:3*x+3]]

    def get_squ_list(self,squ):
        """
        Returns the sub-square squ in list format.

        get_squ_list([[int]]) -> [int]
        """
        return [n for row in squ for n in row]

    def possib(self):
        """
        Updates self._poss to contain all the possible solutions in each
        position of the sudoku.

        possibilities() -> None
        """
        for a,row in enumerate(self._sudoku):
            for b,n in enumerate(row):
                if n == 0:
                    ## Search through the rows
                    for m in self.get_row(a):
                        if self._poss[(a,b)].__contains__(m):
                            self._poss[(a,b)].remove(m)
                    ## Search through the columns
                    for m in self.get_col(b):
                        if self._poss[(a,b)].__contains__(m):
                            self._poss[(a,b)].remove(m)
                    ## Search through the sub-squares
                    for m in self.get_squ_list(self.get_squ(self.get_squ_index(
                        (a,b)))):
                        if self._poss[(a,b)].__contains__(m):
                            self._poss[(a,b)].remove(m)
                    ## Add in the future the ability to search through couplings
                else:
                    self._poss[(a,b)] = [n]

    def solve_poss(self):
        """
        Solves the sudoku puzzle using the possible solutions in each position
        of the puzzle.

        Note:
        poss = possibilities
        pos = position

        solve_poss() -> None
        """
        self._changes_made = False
        for pos in S._poss:
            a,b = pos
            if self._sudoku[a][b] == 0:
                if len(S._poss[pos]) == 1:
                    self._sudoku[a][b] = S._poss[pos][0]
                    self._changes_made = True

    def solve(self):
        """
        Uses all the available methods of solving the sudoku in a while loop to
        solve the puzzle.

        solve() -> None
        """
        while self._changes_made:
            self.possib()
            self.solve_poss()

    def __repr__(self):
        """
        An official representation of the SudokuSolver class.

        SudokuSolver.__repr__() -> str
        """
        return "SudokuSolver()"

S = SudokuSolver()
s = array([[9,2,4,3,0,0,0,0,0],
           [6,0,8,0,5,9,1,0,0],
           [0,5,0,0,8,0,7,0,2],
           [0,4,0,0,7,5,0,0,0],
           [5,1,0,0,0,0,0,7,6],
           [0,0,0,8,6,0,0,4,0],
           [3,0,1,0,2,0,0,8,0],
           [0,0,7,4,9,0,3,0,5],
           [0,0,0,0,0,1,2,6,9]])
##S = SudokuSolver([s1[:] for s1 in s])
##S.print_sudoku()
##S.solve()
##S.print_sudoku()

