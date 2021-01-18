str1 = "ABC"
str2 = "123"

combo = {str1[i] : str2[i] for i in range(0, len(str1)) }
print(combo)

instructor = {
    "name": "Subham",
    "city" : "sans francisco",
    "color" : "blue"
}

instructor_cap = {key.upper() : value.upper() for key,value in instructor.items()}
print(instructor_cap)

#even or odd
my_list = [1,2,3,4,5,6,7,8,9]

my_list_oddeven = {num : ("even" if num % 2 == 0 else "odd") for num in my_list}
print(my_list_oddeven)

## list to dictionary
person =[["name","subham deb"],["job", "CEO"],["city","san francisco"]]

answer = {item[0]: item[1] for item in person}
answer2 = {k:v for k,v in person}
answer3 = dict(person) 