n = 7

for i in range(n):
    for j in range(n):
        if j == 0 or i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()