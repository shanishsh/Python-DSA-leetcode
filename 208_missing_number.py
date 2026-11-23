nums=[0,1]


sum=(len(nums)+1)/2*(len(nums))

sum2=0
for i in range(len(nums)):
    sum2+=nums[i]

print(sum-sum2)