def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

#to test if variables are non numeric
    if not isinstance(x,(int, float, complex)) or not isinstance(y,(int, float, complex)):
        return -1 
    
#to test if variables are both numeric
    elif isinstance(x,(int, float, complex)) and isinstance(y,(int, float, complex)):

        #Swapping values without creating new variables, by using arithmetic
        x = x + y # x is now total of both numbers
        y = x - y # total less y assigns y with the original x value
        x = x - y #  total less original x value will

        print("Variables with swapped values")
        print("x =", x)
        print("y =", y)


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

swap("Apple",10) # returns -1
swap(9,17) # returns x =17, y=9
