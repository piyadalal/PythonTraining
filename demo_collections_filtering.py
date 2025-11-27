#Description: This script demo HOWTO COPY and optionally filter collections using different means
from demo_iterator_loop import students


students = ['vaishnavi', 'wolfgang', 'konrad', 'eric', 'ajie', 'tobias', 'juan', 'nisha']
# ITERATE through the SOURCE list and COPY + FILTER to a destination collection
#
print("-"*80)
print("1. Using an ITERATOR loop + source, if condition (filtering), an expression")

wee_names = []
for name in students: # for loop + source
    if len(name) <= 5: # if condition (optional filtering)
        wee_names.append(name) # expression
print(f"1. Short names = {wee_names}")
print("-"*80)

# 1. Using an ITERATOR loop + source, if condition (filtering), an expression
def filter_names (name) :
    """ Return True if length of name is ‹ 5 chars """
    if len(name) <= 5:
        return True
    else:
        return False

print("-"*80)
print("2. Using built-in filter() function + source, user function (filtering) : filter_names, collection should be passed one element after another")

wee_names = []
for name in students:
    if filter_names(name) :
        wee_names.append(name)
print(f"2. Short names = {wee_names}")


print("-"*80)
print("3. Using built-in filter() function + source, user function (filtering) : filter_names, collection should be passed one element after another")

# 3. Using built-in filter() function + source, user function (filtering) : filter_names
wee_names = list(filter(filter_names, students))
print(f"3. Short names = {wee_names}")



print("-"*80)
print("4. Using built-in filter() function + source, lambda function (filtering)")


# 4. Using built-in filter() function + source, lambda function (filtering)
wee_names = list(filter(lambda name: len(name) <= 5, students)) # replaced filter_names function with lambda inline function
print(f"4. Short names = {wee_names}")



print("-"*80)
print("5. Using LIST COMPREHENSION : expression/return, for loop + source, optional condition (filtering)")


# 5. Using LIST COMPREHENSION : expression/return, for loop + source, optional condition (filtering)
# give me all the names in students if length is less than 5
wee_names = [name for name in students if len(name) <= 5]
print(f"5. Short names = {wee_names}")
print("-"*80)

print("5.1 Using LIST COMPREHENSION : with additional logic pre-processing before adding to list")


# 5. Using LIST COMPREHENSION : expression/return, for loop + source, optional condition (filtering)
# give me all the names in students if length is less than 5
wee_names = [(name.upper(), len(name)) for name in students if len(name) <= 5]
print(f"5. Short names = {wee_names}")
print("-"*80)


print("5.2 Using DICT COMPREHENSION freebee duplicate keys removed: with additional logic pre-processing before adding to list")


# 5.2 Using DICT COMPREHENSION : expression/return, for loop + source, optional condition (filtering)
# give me all the names in students if length is less than 5

wee_names = {name.upper() : len(name) for name in students if len(name) <= 5}
print(f"5. Short names = {wee_names}")
print("-"*80)

