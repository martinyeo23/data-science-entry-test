def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # check if both variables are numeric
    if isinstance(num,(int,float,complex)) and isinstance(divisor,(int,float,complex)):
        # return True is divisible, False otherwise      
        return num%divisor==0
        # return message if either variable is not numeric       
    else: 
        return print("Both num and divisor must be numeric")


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
check_divisibility(10, 2) #returns True
check_divisibility(7, 3) #returns False
