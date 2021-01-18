#Create a function that given a string, it returns the middle character of the string. If the length of the string is even, return the two middle characters of the string.
def middle(string):
    middle_string=""
    if len(string)%2 == 1:
        
        middle_string = string[int(len(string)/2)]
    else:
        
        middle_string = string[int(len(string)/2)]+string[int(len(string)/2)-1]

    return middle_string

