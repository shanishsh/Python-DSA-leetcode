# digits=[9,9,9]

# number=0
# power=len(digits)-1
# for i in range(power,-1,-1):
#     number=number+digits[power-i]*(10**i)

# number+=1


# new_arr=[]

# for i in range(power,-1,-1):
#     digit=number//10**i
#     number-=digit*10**i
#     if digit==10:
#         new_arr.append(1)
#         new_arr.append(0)
#     else:
#         new_arr.append(digit)   



## Optimised code 

arr = [1,2,3]
arr_length=len(arr)

for i in range(arr_length-1,-1,-1):
    if arr[i]==9 :
        arr[i]+=1

    else:
        arr[i]+=1
        break

    if arr[i]==10 and i!=0:
        arr[i]=0


new_arr=[]
for i in range(arr_length):
    if arr[i]==10:
        new_arr.append(1)
        new_arr.append(0)
    else:
        new_arr.append(arr[i])
    

print(new_arr)




    