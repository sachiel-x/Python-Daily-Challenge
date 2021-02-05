# Given a string, create a function that splits the string into pairs of two characters. Put the pairs inside a list then return the list. If a character is missing in a pair, use the character '?' to replace the missing character.

# Example:

# Input: "abcdefg"
# Output = ["ab", "cd", "ef", "g?"]

# Input: "abcdef"
# Output = ["ab", "cd", "ef"]

import re
s1="abcdefg"
l1=[]

l1 = re.findall('..?', s1)

if len(l1[-1])==1:
    l1[-1]=l1[-1]+"?"

print(l1)
    
