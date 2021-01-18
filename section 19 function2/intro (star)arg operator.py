### *arg 
def sum_all_nums(num1,num2,num3):
    total = num1+num2+num3
    return total

print(sum_all_nums(1,2,3)) ##i can't pass morethan 3 arguments

####using *arguments

def sum_all_nums2(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums2(1,2,3,4,5,6,7,8,9,10,11,12,13)) ##how much i want


#####using **kwargs ##keyword arguments

def favoritecolor(**kwargs):
    for key,value in kwargs.items():
        print (f"{key} favorite color is {value}")

favoritecolor(subham="red",babai="black", subhamdeb="black")

#########Parameter Ordering ====>>>> parameters(single), *args, default Parameters, **kwargs


##tuple unpacking or list unpacking
def sumOFallValue(*argus):
    print(argus)

numss = [1,2,3,4,5,6,7]
sumOFallValue(numss) ##returns ([1,2,3,4,5,6,7])
sumOFallValue(*numss) ##returns (1,2,3,4,5,6,7) ##unpaking the list or tuple using * added to the name


##dictionary unpacking
def add_and_multiply_numbers(a,b,c):
    print(a+b*c)

data = dict(a=1,b=2,c=3) ##{'a':1,"b":2, "c":3}

add_and_multiply_numbers(**data) ##data separated as a=1, b=2, c=3