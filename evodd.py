n = int(input())
if n % 2 == 0:
    if n in range(2,5,1):
        print("Not Weird")
    if n in range(6,21,1):
        print("Weird")
    if n > 20:
        print("Not Weird")
#elif n%2 == 1:
else:
    print("Weird")