arr=[5,6,2,3,5,7,8,9]
length=len(arr)-1
k=10

for i in range(k):
    temp=arr[length]

    for j in range(length+1):
        if length-1-j==-1:
            # print("hello")
            break

        arr[length-j]=arr[length-1-j]
        # print(arr)

    arr[0]=temp
    # print(temp)

print(arr)
# print(arr)