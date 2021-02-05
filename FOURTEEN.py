# Given a list of integers, split the list into two, put the arrays on top of each other, then add them together. Return the finished list.

# Example:
# Input:
# [1, 2, 3, 4, 5, 6, 7]

# Putting on top:
# [1, 2, 3]
# [4, 5, 6, 7]

# Adding up process:

# [1, 2, 3]
# +
# [4, 5, 6, 7]
# ------------
# [5, 7, 9, 7]

# Returns:
# [5, 7, 9, 7]

l=[1, 2, 3, 4, 5, 6, 7]
l1=[]
l2=[]
l3=[]

for i in range(0, len(l)//2):
    l1.append(l[i])

for i in range(len(l)//2, len(l)):
    l2.append(l[i])

for i in range(0, len(l1)):
    l3.append(l1[i]+l2[i])

if len(l2) > len(l1):
    l3.append(l2[-1])

# print(l)
# print(l1)
# print(l2)
print(l3)
