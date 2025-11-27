def frange(start,stop,step=0.25):
    """

    :param start: start value
    :param stop: stop value
    :param step: increment value
    :return: next value in the range using yield
    """

    if step == 0:
        return # empty list
    else:
        # check for positive or negative step
        if step > 0:
            while start < stop:
                yield round(float(start),10)
                start += step
        else:
            while start > stop:
                yield round(float(start),10)
                start += step

#Test Conditions
print(list(frange(1.1, 3)))
print(list(frange(1, 3, 0.33)))
print(list(frange(1, 3, 1))) # Should print [1.0, 2.0]
print(list(frange(3, 1))) # Should print an empty list
print(list(frange(1, 3, 0))) # Should print an empty list
print(list(frange(-1, -0.5, 0.1)))
for num in frange(3.142, 12):
         print(f"{num:05.2f}")

print(frange(1,2))


