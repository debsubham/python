import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second ## =====>>>>> precessing will pause in this line and hold for your comment
third = "Third"
result += third

print (result)


########### Instruction ############
# import pdb
# pdb.set_trace()

###### Common PDB commands ######
# l (list)
# n (next line)
# p (print)
# c (continue - finish debugging)