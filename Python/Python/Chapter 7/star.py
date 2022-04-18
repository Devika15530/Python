from signal import pthread_kill


n=int(input())
for i in range(n):
    for j in range(1,n,2):
        print("*")
print("")