##tupple values coude not be change

months = ("January","February","March","April","May","June","July","August", "September", "October","November","December")

for month in months:
    print(month)

print("################Desending####################")

i = len(months) - 1
for month in months:
    print(months[i])
    i -= 1

ii = - 1
for month in months:
    print(months[ii])
    ii -= 1

#############Tuple Count##########
x= (1,2,3,4,5,3,6,4,3,3,3,3,3)

x.count(1) # 1 ##count 1 times 1 is in the tuple
x.count(3) # 7 ##count 7 times 3 is in the tuple

############Tuple Index#############
x.index(1) # 0
x.index(5) # 4
x.index(3) # 2 ##only return index of first matching item

##############Some Extras Tuple Methods############

nums = (1,2,3,(4,5),6,7,8,9,10)
nums[0] # 1
nums[3] # (4,5)
nums[3][1] # 5

# print(nums[0:]) ##(1, 2, 3, (4, 5), 6, 7, 8, 9, 10)
# print(nums[0:4]) ##(1, 2, 3, (4, 5))
print(nums[0:9:3]) ####will search in web for information


