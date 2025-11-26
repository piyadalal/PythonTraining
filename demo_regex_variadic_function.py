print("-" * 50 + "* in function parameters (TUPLE)" + "-" * 50)
import re
# Example of a VARIADIC function that allows variable
# number of parameters - captured in a TUPLE!|

def search_pattern(pattern = "^.{19}$", *files):
    lines = 0
    for file in files:
        fh_in = open (file, mode="rt")
        for line in fh_in:
            m = re. search(pattern, line)
        # Match lines of exactly 19 chars
            if m:
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
                lines += 1
            fh_in. close()
    return lines

num_lines = search_pattern(r"^([A-Z]).*\1$", r"words", r"words2")
print(f"Lines matched = {num_lines}")