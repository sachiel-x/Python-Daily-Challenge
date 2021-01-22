# Given two integer inputs n and d, create a function that squares all numbers from 1 to n, then returns the count of all instances of d from the square results.  

# Example: 

# n: 5
# d: 1

# square of numbers from 1 to 5: 1, 4, 9, 16, 25
# returns: 2 (since there's 2 instances of the digit 1, in 1 and 16)

def sq_count(num, dig):

    l1=[]
    s1=""
    c=str(dig)
    count=0


    for i in range(1, num+1):
        l1.append(str(i**2))

    s1="".join(l1)

    for i in s1:
        if i == c:
            count += 1

    return count

sq_count(5, 1)