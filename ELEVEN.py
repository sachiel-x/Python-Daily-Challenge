# Given a string, return the character with the most value. 
# The value of a character is the difference between the index of its first occurrence 
# and the index of its last occurrence. 
# If there is a tie, return the character that goes first alphabetically.

# Example:
# Input: 'abcdbcd'
# Output: 'b', since difference between first index and last index = 4 - 1 = 3, 
# which ties with the values of c and d but since b goes first alphabetically, 
# that's the most valuable character.

str1 = 'abcdbcdabcdbcd'

d1={}

for i, j in enumerate(str1):
    if j in d1:
        d1[j].append(i)
        
    else:
        d1[j]=[i]

k1 = list(d1.keys())

d2={}

for i in k1:
    d2[i]=max(d1[i])-min(d1[i])

itemsList=d2.items()

k2=[]

for i in itemsList:
        if i[1] == 10:
            k2.append(i[0])

print(f"the character with the most value is: {min(k2)}")