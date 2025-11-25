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
        line = line.rstrip()  # remove trailing newline and spaces
        if not line or not line.startswith('M'):
            continue  # skip empty lines or non-Messier lines

        # Fixed-width slicing based on the format you provided
        messier_number = line[0:5].strip()        # MessierNumber column
        common_name = line[5:38].strip()         # CommonName column
        object_type = line[38:63].strip()        # ObjectType column
        constellation = line[63:].strip()        # Constellation column

        # Handle missing common name
        if not common_name:
            common_name = 'no name'

        # Print using | delimiters
        print(f"|{messier_number}|{common_name}|{object_type}|{constellation}|")
