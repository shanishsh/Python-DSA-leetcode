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
k=3


if k<=len(arr):
    new_arr=arr[-k:]
    print(arr[:-k])

    for i in range(len(arr[:-k])):
        new_arr.append(arr[i])

        # arr=new_arr

    # print(new_arr)

else:
    new_k=k%len(arr)
    # print(arr[:-new_k])
    new_arr=arr[-new_k:]

    for i in range(len(arr[:-new_k])):
        new_arr.append(arr[i])


print(new_arr)


