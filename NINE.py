# Given a string, add or subtract numbers and return the answer.

# Example:
# Input: 1plus2plus3minus4
# Output: 2
# Input: 2minus6plus4plus7
# Output: 7

import re
x="2minus6plus4plus7"
l1=[]
x1=""
for c, i in enumerate(x):
    if i.isnumeric():
        l1.append(int(i))
            

for i in x:
    if i.isnumeric():
        x1+=" "
    else:
        x1+=i

l2=x1.split()

summ=int(l1[0])

for i in range(len(l2)):
    if l2[i] == "plus":
        summ+=l1[i+1]
        
    else:
        summ-=l1[i+1]

print(summ)