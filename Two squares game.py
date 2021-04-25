N = 4
grid = [["." for i in range(N)] for j in range(N)]
score = [0, 0]


def print_grid():
    print('-' * ((N + 4) * N + N + 1))
    for i in range(N):
        print(end='|')
        for j in range(N):
            str_len = len(str(grid[i][j]))
            r1 = ((N + 4) - str_len + 1) // 2
            r2 = ((N + 4) - str_len) - r1
            e = (' ' * r1) + str(grid[i][j]) + (' ' * r2)
            print(e, end='|')
        print()
        print('-' * ((N + 4) * N + N + 1))



def check_full_grid():
    for i in range(N):
        for j in range(N-1):
            if grid[i][j]=="." and grid[i][j+1]==".":
                return False
    for i in range(N-1):
        for j in range(N):
            if grid[i][j]=="." and grid[i+1][j]==".":
                return False
    return True


def check_tie():
    pass
    #if check_full_grid() and score[0]==4 and score[1]==4:
        #return True
    #return False


def is_valid_position(i,j,k,l):
    if (0>i or i>3):
        return False
    if (0>j or j>3):
        return False
    if (0>k or k>3):
        return False
    if (0>l or l>3):
        return False
    if grid[i][j] == "X" or grid[k][l] == "X":
        return False
    if k != i and k != i-1 and k != i+1:
        return False
    if l != j and l != j-1 and l != j+1:
        return False
    if i==k and j==l:
        return False
    if i!=k and j!=l:
        return False
    return True


def set_cell(i, j, k, l):
    grid[i][j] = 'X'
    grid[k][l] = 'X'


def check_win():
    if check_full_grid():
        return True
    return False


def clear_grid():
    for i in range (N):
        for j in range (N):
            grid[i][j]='.'


def play_game():
    print("two squares Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        print("player %s turn" % player)
        print_grid()
        i, j = map(int, input('Enter the row index and column index for the first cell: ').split())
        k, l = map(int, input('Enter the row index and column index for the second cell: ').split())
        print()

        while not is_valid_position(i,j,k,l) :
            print("enter valid cells")
            i, j = map(int, input('Enter the row index and column index for the first cell: ').split())
            k, l = map(int, input('Enter the row index and column index for the second cell: ').split())
            print()

        set_cell(i,j,k,l)
        if check_win():
            print("player %s won" % player)
            break

        player = 1 - player

while True:
    clear_grid()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
