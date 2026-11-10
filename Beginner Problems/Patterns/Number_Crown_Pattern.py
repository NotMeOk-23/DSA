N = int(input("Enter a number: "))

for i in range(N):
    for j in range(1, i+2):
        print(j, end=" ")
    for j in range(2*(N-i-1)):
        print(" ", end=" ")
    for j in range(i+1, 0, -1):
        print(j, end=" ")        
    print()

