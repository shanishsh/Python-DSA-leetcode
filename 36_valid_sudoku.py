board = [
["5", "3", ".", ".", "7", ".", ".", ".", "."],
["6", ".", "3", "1", "9", "5", ".", ".", "."],
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"],
["7", ".", ".", ".", "2", ".", ".", ".", "6"],
[".", "6", ".", ".", ".", ".", "2", "8", "."],
[".", ".", ".", "4", "1", "9", ".", ".", "5"],
[".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

l1=[]
l2=[]
l3=[]
isValid=True

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]==".":
            continue
        if board[i][j] not in l1:
            l1.append(board[i][j])
        else:
            isValid=False
    l1=[]

for i in range(len(board[0])):
    for j in range(len(board)):
        if board[j][i]==".":
            continue
        if board[j][i] not in l2:
            l2.append(board[j][i])
        else:
            isValid=False
    l2=[]

for i in range(0,9,3):
    for j in range(0,9,3):
        for l in range(i,i+3):
            for m in range(j, j+3):
                if board[l][m]==".":
                    continue
                if board[l][m] not in l3:
                    l3.append(board[l][m])
                else:
                    isValid=False
        l3=[]



print(isValid)