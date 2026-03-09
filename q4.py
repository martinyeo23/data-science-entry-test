def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
        #check is s is a string
    if type(s) == str:
        #to reverse string
          return s[::-1]

    #result if s is not a string 
    else:
        return print("input variable s must be a string")

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
string_reverse("Hello World") #returns 'dlroW olleH'
string_reverse("Python") #returns "Python"
