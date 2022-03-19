import time
def countdown(n):
    if n==0:
        print("Blast Off!")
    else :
        print(n)
        print("*"*n)
        time.sleep(1)
        countdown(n-1)
limit=int(input("Enter a time limit"))
countdown(limit)