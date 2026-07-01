
numbers = [2, 4, 5, 6, 7, 8,  2, 2, 3, 4, 6, 7, 7, 7,7 ,7]

#### find duplicate 

nums = set()

for x in numbers :
    if x not in nums :
        nums.add(x)
    else :
        print(f" Duplicate element : {x}") 
        break 

#### Number of occurance of numebr

nums1 = dict()

for x in numbers : 
    if x in nums1 :
         nums1[x] = nums1[x] + 1
    else :
         nums1[x] = 1

print(nums1.get(3))
print(nums1)

print (nums1.keys() )

