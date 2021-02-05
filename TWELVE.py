# Given a list of 5 floats, return a tuple of the average of the middle 3 floats and the lowest float of that list.

# Example:

# Input:
# [6.4, 11.4, 7.6, 10.5, 8.1]

# Returns:
#  (9.83, 6.4), 9.83 (rounded off to nearest two decimal places) is the average of 11.4, 7.6 and 10.5 and 6.4 is the lowest float of the list.

from statistics import mean 

def action(l1):
    avg = mean([l1[1], l1[2], l1[3]])
    avg = round(avg, 2)
    return (avg, min(l1))

lii = [6.4, 11.4, 7.6, 10.5, 8.1]

action(lii)