digits=[9,9,9]

number=0
power=len(digits)-1
for i in range(power,-1,-1):
    number=number+digits[power-i]*(10**i)

number+=1


new_arr=[]

for i in range(power,-1,-1):
    digit=number//10**i
    number-=digit*10**i
    if digit==10:
        new_arr.append(1)
        new_arr.append(0)
    else:
        new_arr.append(digit)   

new_arr 


    