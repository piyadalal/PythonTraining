# Open the file with latin-1 encoding
for line in open('messier.txt', encoding='latin_1'):
    if not line:
        break
    else:
        if not line.startswith('M'):
            continue


        fields = line.split()  # Default splits on whitespace
        print(fields)


        messier_number = fields[0]


        if len(fields) == 4:
            common_name = fields[1]
            object_type = fields[2]
            constellation = fields[3]
        elif len(fields) == 3:
            common_name = 'no name'
            object_type = fields[1]
            constellation = fields[2]
        else:
            # Handle unexpected format
            continue

        # Print using '|' delimiters
        #print(f"|{messier_number}|{common_name}|{object_type}|{constellation}|")
