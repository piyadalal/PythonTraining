import re

fh_in = open(r"/Users/prda5207/PycharmProjects/PythonTraining/VM_code/words", mode="rt")
# for line in fh_in:
#     if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
#         print(line, end="")


for line in fh_in:
    #m = re.search("^ring$")
    #m = re.search("^.ing$", line)
    # Match lines of 4 chars ending with 'i x2 ^ v
    #m = re.search("^.ing$", line)
    # Match lines of 4 chars ending with 'ing'
    #m = re.search("^...................$", line)  # Match lines of EXACTLY 19 chars
    #m = re.search("^[A-Z]", line)  # Match lines starting with a CAPITAL
    #m = re.search("[0-9][0-9]", line)  # Match lines with 2 consecutive digits
    #m = re.search("[^0-9][0-9][0-9][^0-9]", line)  # Match lines with ONLY 2 consecut
    #m = re.search("[aeibu][aeiou][aeiou]", line)  # Match lines with 4 consecutive vo
    #m = re.search("[aeibu]{3}", line)  # Match lines with exact 3 consecutive vo
    #m = re.search("[aeibu]{3,}", line)  # atleast 3 consecutive vowels
    #m = re.search("[aeibu]{0,3}", line)  # atmost 3 consecutive vowels
    #m = re.search("[aeibu]{0,3}", line)  # atmost 3 consecutive vowels
    #m = re.search(r"\.", line)  # Match lines with a DOT without backslash considered as escape
    #m = re.search("^[A-Z].*[A-Z]$", line)  # Match lines starting with a CAPITAL
    #m = re.search("^[A-Z].?[A-Z]$", line)  # Match lines starting with a CAPITAL and end with caps maybe one or none
    #m = re.search("[A-Z]$", line)  # ending with caps
    m = re.search(r"^(.)(.).\2\1$", line) # takes 2 and 1 as escape : \2 : \u0002 : \x02 : \2, put an r as raw string
    #m = re.search(r"^([A-Z]).*\1$", line) # takes 2 and 1 as escape : \2 : \u0002 : \x02 : \2, put an r as raw string
    #r"^(.) (.) (.) \3 \2 \1$"

    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}" f" Groupings = {m.groups()}, Group 1 = {m.group(1)}")
        #print(line, end="")
