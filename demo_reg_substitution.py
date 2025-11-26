import re

line = r"root:x:0:0:The Super User:/root:/bin/zsh" # if backslash use raw string


re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line)
re.sub(r"ksh$", r"bash", line)
(line, num) = re.subn(r".sh$", r"bash", line) # retruns a TUPLE (modified str, num changes)
print(f"Modified line: {line} with {num} changes")
