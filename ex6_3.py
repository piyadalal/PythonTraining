# Read the area-district to country mapping
import re

valid = open('validpc.txt', 'r').read().splitlines()

# Create dictionary: key = area-district, value = country
area_country = {}
for txt in valid:
    # Each line has format "AB1,Scotland"
    parts = txt.strip().split(",")
    if len(parts) == 2:
        area_country[parts[0].upper()] = parts[1]  # ensure uppercase for matching


# Regex with a capture group for area-district (everything before space)
postcode_pattern = re.compile(
    r'^([A-Z]{1,2}[0-9]{1,2}[A-Z]?)\s[0-9][A-Z]{2}$'
)

valid_count = 0
invalid_count = 0

with open('postcodes.txt', 'r') as infile:
    for line in infile:
        # Cleanup: remove whitespace/tabs/newlines
        postcode = re.sub(r'\s+', '', line).upper()
        if not postcode:
            continue

        # Insert space before the last 3 characters
        if len(postcode) > 3:
            postcode = postcode[:-3] + ' ' + postcode[-3:]

        # Validate and capture area-district
        m = postcode_pattern.match(postcode)
        if m:
            area_district = m.group(1)  # captured area-district
            country = area_country.get(area_district, "Unknown")  # lookup country
            print(f"{postcode}  VALID  Country: {country}")
            valid_count += 1
        else:
            print(f"{postcode}  INVALID")
            invalid_count += 1

# Totals
print(f"\nTotal valid postcodes: {valid_count}")
print(f"Total invalid postcodes: {invalid_count}")

