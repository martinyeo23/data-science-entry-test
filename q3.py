#Answer
def update_dictionary(dct, key, value):
    
    if dct.get(key)== None:
        dct[key]=value
        return dct
    if not dct.get(key)== None:
        old_value = dct[key]
        dct[key] = value
        return print(old_value,dct)

update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)

#Question
def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
