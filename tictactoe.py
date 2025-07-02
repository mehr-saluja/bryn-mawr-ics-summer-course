board = [
    [".",".","."],  
    [".",".","."],  
    [".",".","."]]  



player = "X" 



def printBoard(grid): 
    for row in grid:
        print("|",end = "")
        for number in row:
            print(number, end = "|")
        print()

def checkWinner(current_player,grid): 
    for i in range(len(grid)): 
        if grid[i][0] == grid[i][1] == grid[i][2] == current_player:
            print(f"Player {current_player} wins with a row!")
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == current_player:
        print(f"{current_player} wins with a left diagonal!")
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == current_player:
        print(f"{current_player} wins with a right diagonal!")
        return True
    for i in range(len(grid[0])):
        if grid[0][i] == grid[1][i] == grid[2][i] == current_player:
            print(f"{current_player} wins with a column!")
            return True

def switchPlayer(current_player): 
    if current_player == "X":
        return "O"
    elif current_player == "O":
        return "X" 
def main(): 
     board= [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
    ]
     player= "O"
     check= True 
     while check == True: 
        print(f"{player}'s turn")
        printBoard(board)
        row= int(input("Input the row you want to put your piece: "))
        col= int(input("Input the column you want to put your piece: "))
        board[row][col] = player 
        if checkWinner(player, board) == True: 
            check= False
        player= switchPlayer(player)


main ()