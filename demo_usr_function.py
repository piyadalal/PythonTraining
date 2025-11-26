# Description: HOWTO define name and call a function with optional param,  default params and
import pickle

message = "hello" + " " + "my friends"
print(message)
#code
message = "hello" + " " + "my friends"
print(message)
#code
message = "hello" + " " + "my friends"
print(message)


print("-" * 50 + "How to optimize it using functions" + "-" * 50)

def say_hello(): #
    message = "hello" + " " + "my friends"
    print(message)
    return # auto stops indentation # implicit return is available (which returns Noene) (but explicit better than implicit


say_hello()
say_hello()
say_hello()

print("-" * 50 + "Function using Parameters in called and arguments in caller" + "-" * 50)
print("-" * 50 + "Positional Parameter passing" + "-" * 50)

def say_hello(greeting, recipient): #
    message = f"{greeting} {recipient}"
    print(message)
    return None# auto stops indentation # implicit return is available (which returns Noene) (but explicit better than implicit

#say_hello() #missing 2 required positional arguments: 'greeting' and 'recipient
say_hello("hello", "my friends")

print("-" * 50 + "Named Parameter passing" + "-" * 50)

def say_hello(greeting, recipient): #
    message = f"{greeting} {recipient}"
    print(message)
    return None# auto stops indentation # implicit return is available (which returns Noene) (but explicit better than implicit

#say_hello() #missing 2 required positional arguments: 'greeting' and 'recipient

say_hello(greeting="hello", recipient = "mein freunde")

print("-" * 50 + "Mixed Parameter passing : Positional comes before named Params passing" + "-" * 50)

def say_hello(greeting, recipient): #
    message = f"{greeting} {recipient}"
    print(message)
    return None# auto stops indentation # implicit return is available (which returns Noene) (but explicit better than implicit

#say_hello() #missing 2 required positional arguments: 'greeting' and 'recipient

say_hello("hello", recipient = "mein freunde")

print("-" * 50 + "Default Param" + "-" * 50)

def say_hello(greeting, recipient = "mein freunde"):  #
    message = f"{greeting} {recipient}"
    print(message)
    return None# auto stops indentation # implicit return is available (which returns Noene) (but explicit better than implicit

#say_hello() #missing 2 required positional arguments: 'greeting' and 'recipient

say_hello("hello")

print("-" * 50 + "Named param passing after *" + "-" * 50)

def say_hello(greeting, * , recipient = "mein freunde"):  #
    message = f"{greeting} {recipient}"
    print(message)
    return None# auto stops indentation # implicit return is available (which returns Noene) (but explicit better than implicit

#say_hello() #missing 2 required positional arguments: 'greeting' and 'recipient

say_hello("hello")

print("-" * 50 + "Mutable lists as default arguments always use None" + "-" * 50)


def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # ?
print(add_item(2))  # ?



def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(add_item(1))
print(add_item(2))




