#################################################################################################
#######################################Dictionary Methods########################################
#################################################################################################


## k,v in instructor.items ## .copy ## .clear ## .fromkeys("a", "b")##.get("name")##.pop##.popitems##.update ##
instructor = {
    "name": "Subham",
    "city" : "sans francisco",
    "color" : "blue"
}

instructor_cap = {key.upper() : value.upper() for key,value in instructor.items()} ##method 1
print(instructor_cap)
# output - {'NAME': 'SUBHAM', 'CITY': 'SANS FRANCISCO', 'COLOR': 'BLUE'}

str1 = "ABC"
str2 = "123"

combo = {str1[i] : str2[i] for i in range(0, len(str1)) } ##method 1
combo_output = dict(zip(str1,str2))
print(combo)
##output - {"A":"1","B":"2","C":"3"}


## list to dictionary
person =[["name","subham deb"],["job", "CEO"],["city", "San Francisco"]]

answer = {item[0]: item[1] for item in person} ##method1
answer2 = {k:v for k,v in person}##method2
answer3 = dict(person) ##method3
 ##output - {"name" : "subham", "job" : "CEO", "city": "San Francisco"}















###########################################################################################################
###############################################Tuples And Sets#############################################
###########################################################################################################

##can not be change values

alphabet = ("a","b","c","d")
 #alphabets[1] = "c" ##ypu can't do that +++ value not gonna change

months = ("January","February","March","April","May","June","July","August", "September", "October","November","December")

for month in months:
    print(month)


i = len(months) - 1     ###################
for month in months:    ##Desending order##
    print(months[i])    ###################
    i -= 1              ###################



#############################################################################
######################################Sets###################################
##orderless(no indexing) ##Like mathematicical sets  

s ={1,2,3,4,5,5,4} ##returnd {1,2,3,4,5} only unique values
s2 ={1,5,7,6,3,"a","b","d"}

for item in s2:
    print(item)

s3 = [1,2,3,4,5,6,7,8,9,1,2,4,5,6,7,5,4,4,4,6,6,3,4] ##some number is repeat
print(f"before {s3}")
print(set(s3)) ##only one time print every unique values
s3 = list(set(s3))
print(f"after {s3}")

cities = {"Kolkata"}
print(cities)
cities.add("barasat") ##add item to the set ### cities.discard("barasat") its also same and no error if not found
cities.remove("barasat")
print(cities)

set1={1,2,3,4,7,8,9}
set2 = {1,2,3,4,5,6}
print(set1 | set2) ##union of set
print(set1 & set2) ##intersection of sets


#############################################################################
strings = "hello"
{char for char in strings if char in "aeiou"} ## {"e","o"}



###########################################################################################################
###################################################Function################################################
###########################################################################################################


def myfunc():
    print("hello")
myfunc()

#####return####exaple FLIP A COIN
##random import
form random import random
def flip_coin():
    if(5 > random()*10):
        print("Head")
    else:
        print("tail")


############
total = 0
def sayHello():
    instructor = "subham" ##this is a SCOPE that only valid for this function
    global total
    total =+ 1 ##value change because we use total as global variable
    return f'Hello {instructor}'

##print(instructor) ##its not working because instructor is not defined globaly


#####usefull features#####
def myfunction2():
    """here the documents about the function its very usefull"""
    print("Hello")

print(myfunction2())
print(myfunction2.__doc__)


##### *arg ######
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

print(sum_all_nums2(1,2,3,4,5,6,7,8,9,10,11,12,13)) ##pass how much i want


#####using **kwargs ##keyword arguments

def favoritecolor(**kwargs): ##**kwargs store input arguments as a diationary
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




########################################################################################
##############################Lamdas and builtin function###############################
########################################################################################

##lamda is use for inline function that only excuted once or only for specific button
##Example  ===>   when i click a button Onclick = lambda : print("button click")
lamdafuction = lambda a,b : a+b ##lamdafunction add a+b 

#######map#######
singles = [1,2,3,4,5]
doubles = list(map(lambda x: x*2, singles))

#######Filter######

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

evenlist = list(filter(lambda x : x % 2 == 0, nums))

print(evenlist)

##i can use map filter in one functiong



##all is true or false

nums = [2,4,6,8,10,12,14,18,56]
nums2 = [1,2,3]
#if all numbers even all is true

result = all(map(lambda x : x%2 ==0, nums)) ##false if atleast one is false /// true if whole things is true
print(result) 

print(any(val for val in nums2 if val < 5))  ##true if one is true
print(any(val for val in nums2 if val > 4))  ##false if whole is false


############sort() and sorted##########

####sorted  (works on anything that is iterable)

more_numbers = [6,8,1,6,9,4,3,7,2,1]
print(sorted(more_numbers)) ## [1, 1, 2, 3, 4, 6, 6, 7, 8, 9]  ##=>> not change the initial values serial
more_numbers.sort() ###output is same but change the values serial in more_numbers

print(sorted(more_numbers, reverse=True)) ## reverse order

users = [{
        "name" : "Subham",
        "title" : "Deb",
        "address" : "amd",
        "count" : 19
    },
    {
        "name" : "Subham deb",
        "adderss" : "merua",
        "title" : "Deb",
        "count" : 12
    },
    {
        "name" : "Subham",
        "title" : "Deb",
        "address" : "amd",
        "count" : 55
    },
    {
        "name" : "Subham",
        "title" : "Deb sfgasdgasdg",
        "address" : "amdfgasgag",
        "count" : 8
    },
    {"name" : "Subham",
        "title" : "Deb",
        "address" : "Merua, Amadpur, Memari",
        "count" : 2}

]


print(sorted(users, key=len)) ##sort by length of dictionaries

print(sorted(users, key=lambda x : x["count"])) ## sorted by count key

######min max######


######reversed######



######len() // "subham".__len__()

print(len("subham")) ##6
print(len({"a":1,"b":2,"c":3,"sdf":"sfsf"})) ##4

name = "Subham Deb"
print(name.__len__()) ##10
print("Subham deb".__len__()) ##10


#####abs#####
##magnitude of this number
abs(-5) ##5
abs(5) ##5

#####sum####

sum([1,2,3])
print(sum([1,2,3],10)) ##16
print(sum([1,2,3,4,5],-10)) ##5

######round######
round(4.321) ##4
round(4.58642) #5
round(3.52462481, 3) ## 3.524


######################################################################
##############################################################
######################################################################


########################################################################
################################# Modules ##############################
########################################################################






#########################################################################
############################## Https request ############################
#########################################################################

import requests

url = "http://icanhazdadjoke.com/search"


print("Let me tell yoou a joke! Give me a topic:::")

answer = input("Answer ")

response = requests.get(url, headers={"Accept" : "application/json"}, params={"term" :answer, "limit" : 1})

total = response.json()["total_jokes"]

print(f"i have got {total} jokes about {answer}. Here's one::")
print(response.json()["results"][0]["joke"])










######################################################################
################################ OOP #################################
######################################################################

class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"
    def short_name(self):
        return f"{self.first[0]} {self.last[0]}"
    def likes(self , things):
        return f"{self.first} likes {things}"


user1 = User("Subham","Deb", 23)

print(user1.full_name())
print(user1.short_name())

print(user1.likes("Chicken")) ##only pass the things and it will automaticly fetch in User's methods


####################

class Pet:
    allowed = ["cat", "dog", "fish", "rat"]
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"you can't have a {species}")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"{species} not allowed")
        self.species = species
        
    

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
print(cat.species)

cat.set_species("rat")
print(cat.species)



##############

class User:
    active_users = 0
    @classmethod
    def _dispaly_active_users(cls):
        return f"there are currently {cls.active_users} active users"

    @classmethod
    def form_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last, int(age))

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age


#########

class User:
    pass


user1 = User() ##all instance are in diffrents locations


user1 = User()
user1 = User()
user1 = User()



##################

class User:
    total_online = 0
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.total_online += 1

    def full_name(self):
        return f"{self.first} {self.last}"
        
    def short_name(self):
        return f"{self.first[0]} {self.last[0]}"
    def likes(self , things):
        return f"{self.first} likes {things}"
    def logout(self):
        User.total_online -= 1
        return (f"{self.first}, you are Logged out")


user1 = User("Subham","Deb", 23)

print(user1.full_name())
print(user1.short_name())
print(user1.likes("Chicken")) ##only pass the things and it will automaticly fetch in User's methods


user2 = User("Babai","Deb", 89)

print(user2.full_name())
print(user2.short_name())
print(user2.likes("Mutton"))

print(User.total_online)

print(user2.logout())
print(User.total_online)


#############################

class WithOut_repr:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def print_it(self):
        return f"{self.first} {self.last}"

class With_repr:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def __repr__(self):
        return f"{self.first}"
    def print_it(self):
        return f"{self.first} {self.last}"


user1 = WithOut_repr("suhbham","deb")
print(user1.print_it())
print(user1) ###return address


user2 = With_repr("suhbham", "deb")
print(user2.print_it())
print(user2) ###return self.first























































################################################################################
258 : inheritance example User and Modaretor


































##############################################Iterators and Generators


####Iterators













##### Generators

 def count_up_to(max):
     count = 1
     while count <= max :
         yield count
         count += 1

counter = count_up_to(5)

################# generators exercise

def week():
  allday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  for day in allday:
    yield day


days = week()

print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
# print(next(days))

def yes_or_no():
    condition = "yes"
    while 1 :
        yield ("yes" if condition == "yes" else "no")
        condition = "yes" if condition == "no" else "no"

gen =yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

###############make song exercise

def make_song(how_much=99, what_is="soda"):
  
  
  i=how_much
  while i>=0:
    if(i==1):
      yield f"Only 1 bottle of {what_is} left!"
    elif(i>1):
      yield f"{i} bottles of {what_is} on the wall."
    else:
      yield f"No more {what_is}!"
    i-=1

default_song= make_song(3,"some")

print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))