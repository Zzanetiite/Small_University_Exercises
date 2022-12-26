# String formatting and regular expressions.
import re

infile = open('postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contains the line
    # read from the file.

    # Ignore empty lines.
    if postcode.isspace(): continue

    # TODO (a): Remove newlines, tabs and spaces.
    postcode = postcode.strip().replace(' ', '')

    # TODO (a): Convert to uppercase.
    postcode = postcode.upper()

    # TODO (a): Insert a space before the final three characters
    # (a digit and 2 letters).
    space_location = len(postcode) - 3
    postcode = postcode[0: space_location] + ' ' + postcode[space_location: len(postcode)]



    # TODO (b) Validate the postcode, returning a match object 'm'.
    pattern = '[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1}\s\d[A-Z]{2}'
    m = re.search(pattern, postcode)

    if m:
        valid = valid + 1
        # Print the reformatted postcode.
        print(postcode, ' Valid.')

    else:
        invalid = invalid + 1
        # Print the reformatted postcode.
        print(postcode, ' Invalid.')

infile.close()

# TODO (b) Print the valid and invalid totals.
print('Valid postcodes:', valid)
print('Invalid postcodes:', invalid)
