#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo
"""
    DocString
"""
# Open the file with latin-1 encoding
with open('messier.txt', encoding='latin_1') as file:
    for line in file:
        line = line.rstrip()
        if not line or not line.startswith('M'):
            continue

        messier_number = line[0:5].strip()
        common_name = line[5:38].strip()
        object_type = line[38:63].strip()
        constellation = line[63:].strip()


        if not common_name:
            common_name = 'no name'

        print(f"|{messier_number}|{common_name}|{object_type}|{constellation}|")
