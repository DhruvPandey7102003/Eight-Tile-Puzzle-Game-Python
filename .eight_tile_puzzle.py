import random # "Random" function is used for shuffling the puzzle for each time.

class EightTilePuzzle: # defining a class method 
    def __init__(self): # this is a constructor. it initializes the puzzle.
        
        self.board = self.create_board() # Target set for winning the game.
        
        self.empty_tile = (2, 2)  # it is the current state of the puzzle.

    def create_board(self): # Creating a function for making the board.
        
        numbers = list(range(9))
        random.shuffle(numbers) # Convert the list into a 3x3 board
        return [numbers[i:i + 3] for i in range(0, 9, 3)]

    def display(self): # "Display" function will display the current state of the board.
        
        for row in self.board: # This loops through each row in the board.
            
            print(' '.join(str(num) if num != 0 else ' ' for num in row)) # This converts each number in the row to a string, replaces 
        print()

    def move(self, direction): # "move" method handles empty tile in the specified direction.
        x, y = self.empty_tile
        if direction == 'up' and x > 0: # This checks if the move is "up" and if the empty tile is not in the top row (to prevent moving out of bounds).
            
            self.board[x][y], self.board[x - 1][y] = self.board[x - 1][y], self.board[x][y] # This swaps the empty tile with the tile above it.
            
            self.empty_tile = (x - 1, y) # This updates the position of the empty tile after the move.
            
        elif direction == 'down' and x < 2: # This checks if the move is "down" and if the empty tile is not in the bottom row.
            
            self.board[x][y], self.board[x + 1][y] = self.board[x + 1][y], self.board[x][y] # This swaps the empty tile with the tile below it.
            
            self.empty_tile = (x + 1, y) # This updates the position of the empty tile after the move.
            
        elif direction == 'left' and y > 0: # This checks if the move is "left" and if the empty tile is not in the leftmost column.
            
            self.board[x][y], self.board[x][y - 1] = self.board[x][y - 1], self.board[x][y] # This swaps the empty tile with the tile to the left of it.
            
            self.empty_tile = (x, y - 1) # This updates the position of the empty tile after the move.
            
        elif direction == 'right' and y < 2: # This checks if the move is "right" and if the empty tile is not in the rightmost column.
            
            self.board[x][y], self.board[x][y + 1] = self.board[x][y + 1], self.board[x][y] # This swaps the empty tile with the tile to the right of it.
            
            self.empty_tile = (x, y + 1) # This updates the position of the empty tile after the move.
            
        else: # This handles invalid moves by printing an error message
            print("Invalid move! Try again.")

    def is_solved(self): # this methods checks whether the puzzle is solved.
        correct_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == correct_board

if __name__ == "__main__": # This checks if the script is being run directly
    game = EightTilePuzzle() # we have called our class.
    print("Welcome to the 8-Tile Puzzle Game!")
    game.display() # displays the initial state of the board.

    while not game.is_solved(): # This starts a loop that continues until the puzzle is solved.
        move = input("Enter your move (up, down, left, right): ").strip().lower()
        game.move(move) # specifies the move played by the player.
        game.display() # shows the current state of the board.

    print("Congratulations! You solved the puzzle!")
