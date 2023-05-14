def print_chessboard(m, n) :
    for row in range(m):
        board = ""
        for  clumn in range(n):
            if n % 2 ==0:
               board +="$*"  
            else:
               board+= "*$"
        print(board)
n= int(input("enter n : "))
m= int(input("enter m : "))
print_chessboard(n,m)