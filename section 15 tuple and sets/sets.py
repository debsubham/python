#############################################################################
######################################Sets###################################
##orderless(no indexing) ##Like mathematicical sets  

s ={1,2,3,4,5,5,4} ##returnd {1,2,3,4,5} only unique values
s2 ={1,5,7,6,3,"a","b","d"}

for item in s2:
    print(item)

s3 = [1,2,3,4,5,6,7,8,9,1,2,4,5,6,7,5,4,4,4,6,6,3,4] ##some number is repeat
print(f"before::: {s3}")
print(set(s3)) ##only one time print every unique values
s3 = list(set(s3))
print(f"after::: {s3}")