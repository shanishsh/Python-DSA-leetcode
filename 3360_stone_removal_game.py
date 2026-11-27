n=19
alice=10
bob=alice-1
i=0
while(n>-10):
    if i%2==0:
        n=n-alice
        if n<0:
            print("False")
            break
        alice=bob-1
    else:
        n=n-bob
        if n<0:
            print("True")
            break
        bob=alice-1
    i+=1
