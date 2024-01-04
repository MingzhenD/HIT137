global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Add default parameter: numbers with value [1, 2, 3, 4, 5]
def process_numbers(numbers = list(range(1,6))):
    global global_variable
    # change to length of given list/set
    local_variable = len(numbers)

    while local_variable > 0:
        # check if the collection contains the value before remove it
        if local_variable % 2 == 0 and local_variable in numbers:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Set items are unordered, unchangeable, and do not allow duplicate values.
my_set = {1, 2, 3, 4, 5}
result = process_numbers(numbers=my_set)

# add parameter of this function to modify the dictionary key with default value None
def modify_dict(key, value=None):
    my_dict[key] = value

# modify key4, 10 in my_dict
modify_dict('key4', 10)
# add '5: None' in my_dict
modify_dict(5)

def update_global():
    global global_variable
    global_variable += 10

# call the function by name and parentheses to modify global variable
update_global()

for i in range(5):
    print(i)
    i += 1

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

# check if key set contains 5
if 5 not in my_dict:
    print("5 not found in the dictionary!")

# check if value list contains 10
if 10 not in my_dict.values():
    print("10 not found in the dictionary values!")

print(global_variable)
print(my_dict)
print(my_set)
