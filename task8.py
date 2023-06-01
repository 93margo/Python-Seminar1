print("Введите размер шоколадки n x m ")
n,m=int(input()),int(input())
print("введите количество долек которое хотите отломить")
k=int(input())

if ( k<(n*m) and k%n==0 ) or ( k<(m*n) and k%m==0):
    print(n, m, k, "->", "yes")
else:
    print(n, m, k, "->", "no")