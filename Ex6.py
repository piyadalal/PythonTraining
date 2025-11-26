#! /usr/bin/python
# Exercise 6, string formatting and regular expressions.
import re
from statistics import pstdev

infile = open('postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0
postcode_pattern = re.compile(
    r"[A-Z]{1,2}[0-9]{1,2}[A-Z]?\s[0-9][A-Z]{2}$"
)
for postcode in infile:
    # The variable 'postcode' contain the line read from the file.
    
    # Ignore empty lines.
    if postcode.isspace(): continue

    # TODO (a): Remove newlines, tabs and spaces.
    postcode = postcode.strip()
    print(postcode)
    (postcode, count) = re.subn(r"\s+", "",postcode)
    print(postcode)
    
    # TODO (a): Convert to uppercase.
    postcode = postcode.upper()
    print(postcode)

    # TODO (a): Insert a space before the final digit and 2 letters.
    postcode = re.sub(r"(\d[A-Z]{2})$", r" \1",postcode)
    print(postcode)
    
    # Print the reformatted postcode.
    print (postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'.
    m = re.match(postcode_pattern, postcode)   # TODO (b) Replace this line with a call to re.match().
    
    if m:
        print(f"Valid postcode : {postcode}")
        valid = valid + 1
    else:
        print(f"Invalid postcode : {postcode}")
        invalid = invalid + 1

    # TODO (b) Print the valid and invalid totals.
print(f"Total Valid codes : {valid} and invalid codes : {invalid}")
        

infile.close()



