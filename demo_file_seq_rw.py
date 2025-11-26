#Description : This script will demo howto open for reading writing appending to text or
# #binary files using builtin open() funciton
import sys

movies =  {'eric': ['pulp fiction', 'forest gump', 'platoon'],
'bertwin': ['kill bill', 'hateful 8', 'the firm'],
'stephan': ['james bond', 'Bourne', 'batman']
 }

#open file handle for WRITING in TEXT mode
fh_out = open('movies.txt', mode='wt') #<_io.TextIOWrapper name='movies.txt' mode='wt' encoding='UTF-8'>
#print(fh_out)
#print(type(fh_out))

for name in movies.keys():
    #fh_out.write(name , movies[name])
    fh_out.write(f"{name} {movies[name]} \n") # write doesn't have new line
    #print(f"{name} {movies[name]}", end = "\n") # f strings by default converts the arguments to strings
    #print("Hello", end="\t")
    #print("Hello", end="")      # no newline

fh_out.close() # flushes buffers and closes the file handle

#SEQUENCE READING LINE BY LINE

fh_in = open('movies.txt', mode='rt', buffering=1)
#text = fh_in.read() # whole file is read
#char_30 = fh_in.read(30) # always reads next 30 chars
#line = fh_in.readline() # always reads next line
#fh_in.seek(0) # reset the pointer
#lines = fh_in.readlines() # reads all lines into a list
#line lines[0]

# MEMORY EFFICIENT WAY : iterates through filehandler ( Iterable - next()/__iter__)
for line in fh_in:
    if "eric" in line:
        print(line)
        break

#print(lines)

print("-" * 50)

#print("This goes to stdout", file="output_print.txt") # AttributeError: 'str' object has no attribute 'write'

print("This goes to stdout", file=fh_out)
print("This is an error", file=sys.stderr)

#Block scope to make file handle close automaticlly after block ends
with open("movies.txt", mode='rt', buffering=1) as fh_in:
    for line in fh_in:
        if "eric" in line:
            print(line)
            break
    #end of block file handle will auto close
    # or del fh_in
