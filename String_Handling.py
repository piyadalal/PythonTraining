

s = "  Python   is  fun  "
print(s.split())
print(s.split(" "))

currencies = {"pound": "⁄n{pound sign}"}
print(currencies)

for pos in range(0, 10): #65536
    try:
        #print(chr(pos), end=" ") #chr() is a built-in function that converts an integer Unicode code point into the corresponding character.
        if pos % 10 == 0:
            print()

    except UnicodeError:
        print(" ")

name = "Priya Dalal"
# print(name.center(30, '.'))
# print(name.center(30, '#'))
# print(name.rjust(30, '#')) # right justify
# print(name.ljust(30, '#'))# left justify
#
# try:
#     print(name.index("D"))
# except ValueError:
#     print("No letter found")
#
# try:
#     print(name.index("d"))
# except ValueError:
#     print("No letter found")
#
# try:
#     print(name.find("d")) # returns -1
# except ValueError:
#     print("No letter found")
#
# print(name.encode("ascii", "ignore").decode("ascii", "ignore"))
#
#
# s = "\n \t Hello World \t  Hi \n"
# print(s.strip(" ")) # did not strip newline
# print(s.strip()) # stripped newline
#
# name = "\t Donald Cameron  "
# print(name.strip(" ")) # removes from starting and ending not midlle, therefore rstrip and lstrip
# print(name.strip())
#
# name = 'root:x:0:0:The Super User:/root:/bin/bash '
# print(name.strip())


line = 'root:x:0:0:The Super User:/root:/bin/bash '
# modify the string but str are immutable
#split the string iinto list
fields = line.split(":")
print(fields)
fields[6] = "/bin/zsh"
fields[4] = "The Admin"
print(fields) # retunrs list of new words
joined_fields_with_colon = ":".join(fields)
print(joined_fields_with_colon)
