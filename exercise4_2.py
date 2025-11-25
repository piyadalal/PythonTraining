# Open the file with latin-1 encoding
with open('messier.txt', encoding='latin_1') as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if not line:
            continue  # Skip empty lines
        if not line.startswith('M'):
            continue  # Skip lines not starting with 'M'

        # Split the line into fields
        fields = line.split()  # Default splits on whitespace

        # Messier Number is always the first field
        messier_number = fields[0]

        # Common name: may be missing
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
        print(f"|{messier_number}|{common_name}|{object_type}|{constellation}|")
