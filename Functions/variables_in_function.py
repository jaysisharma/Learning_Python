
# initializing variable at global scope

value = 20

def val():
    value2 = 30 # initializing value in local scope
    return value * value2

print("Function Value", val())

#value2 can not be accessed outside the function
# print(value2)
