# Given a list of integers, create a function that finds the odd one out in the list.
# Example:
# Input: [1,1,1,1,1,1,1,2]
# Output: 2

l1 = [1,1,1,1,1,1,1,2]
d1={}

for i in l1:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1

print()