##all is true or false

nums = [2,4,6,8,10,12,14,18,56]
nums2 = [1,2,3]
#if all numbers even all is true

result = all(map(lambda x : x%2 ==0, nums)) ##false if atleast one is false /// true if whole things is true
print(result) 

print(any(val for val in nums2 if val < 5))  ##true if one is true
print(any(val for val in nums2 if val > 4))  ##false if whole is false

print(any([val for val in nums2 if val < 5]))  ## [] use for only fetch true or false not the result with list (its call genaretor object)
print(any([val for val in nums2 if val > 4]))