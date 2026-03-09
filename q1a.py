#Answer
def swap(x, y):

    if type(x)==int or type(x)==float and type(y)==int or type(y)==float:
            x_new = y
            y_new = x
    elif not type(x)==int or type(x)==float and not type(y)==int or type(y)==float:
            x_new = -1
            y_new = -1
    return print(x_new,y_new)
    
swap("Apple",-3)
swap(9,-17)

#Question
def swap(x, y):

    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

#Answer
