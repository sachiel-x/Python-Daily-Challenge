# Given an integer, create a function that finds and returns the length of the longest binary gap of the binary representation of that integer. A binary gap is the sequence of consecutive zeros in between ones in a binary representation. Reference for binary representation can be found here: https://www.rapidtables.com/convert/number/decimal-to-binary.html

# Example:
# Input: 9, which has binary representation 1001
# Returns: 2
# Input: 529, which has binary representation 1000010001
# Returns: 4
# Input: 20, which has binary representation 10100
# Returns: 1
# Input: 15, which has binary representation 1111
# Returns: 0

def dec_to_bin(x):
    return bin(x)[2:]

num=int(input("Enter a number: "))
s1 = ''
s1 = dec_to_bin(num)
l1 = s1.split("1")
l2=[]

for i in l1:
    l2.append(int(len(i)))

print(f"the max gap is {max(l2)}, binary is {s1}, decimal {num}")