#Rasmus Koskinen

#Sudokun ratkaisija backtracking algorithmillä
board = [ # sudoku haettu iltalehden sudokusta

    [1,0,6,2,7,0,8,0,0],
    [0,0,7,6,0,0,1,0,2],
    [0,5,0,8,0,1,0,4,0],
    [8,2,3,7,1,0,0,0,0],
    [0,0,0,0,0,6,0,7,0],
    [0,0,0,4,0,0,0,8,1],
    [6,0,0,0,9,2,0,0,8],
    [2,1,0,0,0,0,9,5,0],
    [0,0,5,0,0,0,6,0,0]
]


def ratkaise(sudo):
    find = etsi_tyhjat(sudo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if pateva(sudo, i, (row, col)):
            sudo[row][col] = i

            if ratkaise(sudo):
                return True

            sudo[row][col] = 0

    return False


def pateva(sudo, num, sij):
    # takista rivi
    for i in range(len(sudo[0])):
        if sudo[sij[0]][i] == num and sij[1] != i:
            return False

    # tarkista kolumni
    for i in range(len(sudo)):
        if sudo[i][sij[1]] == num and sij[0] != i:
            return False

    # tarkista 3x3
    box_x = sij[1] // 3
    box_y = sij[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if sudo[i][j] == num and (i, j) != sij:
                return False
    return True


def tulosta_sudoku(sudo): # Tulostaa sudokun
    for i in range(len(sudo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sudo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sudo[i][j])
            else:
                print(str(sudo[i][j]) + " ", end="")


def etsi_tyhjat(sudo): # etsii tyhjät ruudut
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            if sudo[i][j] == 0:
                return i, j  # rivi ja kolumni

    return None


tulosta_sudoku(board)
ratkaise(board)
print("***********")
tulosta_sudoku(board)
