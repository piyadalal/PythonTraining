
with open('messier.txt', encoding='latin_1') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if not line.startswith('M'):
            continue


        fields = line.split()


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

            continue


        print(f"|{messier_number}|{common_name}|{object_type}|{constellation}|")
