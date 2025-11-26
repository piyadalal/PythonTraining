import re

fh_in = open(r"/Users/prda5207/PycharmProjects/PythonTraining/VM_code/words", mode="rt") # 45k lines
# for line in fh_in:
#     if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
#         print(line, end="")

re_obj = re.compile(r"^.{19}", flags=re.IGNORECASE) # can use flags in pattern while pre compiling

for line in fh_in:
    m = re.search(r"^.{19}", line) # same pattern repeated for 45k times use precompiled complies pattern only once
    m = re_obj.search(line)
    m = re_obj.search(line)
    try:
        if m:
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
            #print(line, end="")
    except AttributeError:
        print("can't find any matched groups")

