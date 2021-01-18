# Create a function that given an n positive integer, it sums all the cubed values from 1 to n. Return the sum.

def sum_cubes(n):
    sum=0
    for i in range(0, n+1):
        sum+=i**3
        print(sum)

    return sum

sum_cubes(5)