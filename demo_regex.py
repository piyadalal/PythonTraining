import re

fh_in = open(r"C://labs//words", mode="rt")
for line in fh_in:
    if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
        print(line, end="")


for line in fh_in:
    m = re.search("^ring$")
    if m:
        print(line, end="")