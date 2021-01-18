list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = [11,12,13,14,15]

z = zip(list1, list2)

print(f" {z} <===its a tupple coded value ")
print(list(zip(list1,list2, list3))) ###[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(dict(zip(list1,list2))) ##{1: 6, 2: 7, 3: 8, 4: 9, 5: 10}

unzip = zip(*zip(list1,list2)) ##unzip all  ###using star to unzip zip version

print(list(unzip)) 




###################Complex zips#############

final_exam = [80,91,78]
mid_exam = [75,98,50]
student = ["dan","ran","ang"]
final_exam_grade = [max(pair) for pair in zip(mid_exam,final_exam)] ## max number of every pair
print(final_exam_grade)   ## final grade
print({tupp[0]:max(tupp[1],tupp[2]) for tupp in zip(student,mid_exam,final_exam)})


print("++++++++++++++++My version+++++++++++++++")

grade_list=list(map(lambda xx : {xx[0]: max(xx[1],xx[2])} , zip(student,mid_exam,final_exam)))

print(grade_list)


###########################codding exercise 70#########################

# triple_and_filter([1,2,3,4]) # [12]
# triple_and_filter([6,8,10,12]) # [24,36]
# '''

def triple_and_filter(arg):
   numbers = list(map(lambda x: x*3 , filter(lambda xx: xx % 4 == 0, arg)))
   return numbers

############################codeing excercise##########################

# '''
# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
# extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
# '''

def extract_full_name(arg):
    names = list(map(lambda xx : "{} {}".format(xx['first'], xx['last']), arg))
    return names

