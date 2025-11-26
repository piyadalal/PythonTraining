result = 3
def my_func():
    result = 12
    def scope_test():
        nonlocal result # without this UnboundLocalError: cannot access local variable 'result' where it is not associated with a value

        if result < 45:
            result += 1
            scope_test()
    scope_test()
    print(result, "from my_func") # 45 increments recursively

my_func()
print(result, "from main") # 3 global