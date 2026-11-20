# arr=[5,6,2,3,5,7,8,9]
# length=len(arr)-1
# k=10

# for i in range(k):
#     temp=arr[length]

#     for j in range(length+1):
#         if length-1-j==-1:
#             # print("hello")
#             break

#         arr[length-j]=arr[length-1-j]
#         # print(arr)

#     arr[0]=temp
#     # print(temp)

# print(arr)
# # print(arr)


arr=[1,2,3,4,5,6,7]
length=len(arr)
k=15


if k<=len(arr):
    # new_arr=arr[-k:] --- old
    new_arr=arr[:-k]
    count=0
    for i in range(len(arr[-k:])):
        count+=1
        arr[i]=arr[-k+i]

    for i in range(len(new_arr)):
        arr[count]=new_arr[i]
        count+=1


else:
    new_k=k%len(arr)
    # new_arr=arr[-new_k:] --- old
    new_arr=arr[:-new_k]
    count=0

    for i in range(len(arr[-new_k:])):
        arr[count]=arr[-new_k+i]
        count+=1

    for i in range(len(new_arr)):
        arr[count]=new_arr[i]
        count+=1

print(arr)



