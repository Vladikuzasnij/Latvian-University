
def lzw_compress(input_string):
    # Initialize the dictionary with single character strings as keys and their ascii values as values.
    dictionary = {chr(i): i for i in range(256)}
    current_string = ""  # Start with an empty current string.
    result = []  # The output will be a list of codes.
    step = 1

    for symbol in input_string:
        print(f"Step {step}: Current string + symbol = {current_string + symbol}")
        if current_string + symbol in dictionary:  # If the current string followed by the current symbol is in the dictionary,
            current_string = current_string + symbol  # then make that the current string.
        else:  # If the current string followed by the current symbol is not in the dictionary,
            # Add a new entry to the dictionary for the current string followed by the current symbol.
            dictionary[current_string + symbol] = len(dictionary)
            # Output the code for the current string.
            result.append(dictionary[current_string])
            print(f"Output: {dictionary[current_string]}")
            print(f"Add to the dictionary: {len(dictionary) - 256 - 1}: {current_string + symbol}")
            current_string = symbol  # Start a new current string with the current symbol.
        step += 1

    # Output the code for the current string, if it is not empty.
    if current_string:
        result.append(dictionary[current_string])
        print(f"Output: {dictionary[current_string]}")

    print("Final Dictionary:")
    for key, value in dictionary.items():
        if value >= 256:  # Print only the entries that we added during the compression.
            print(f"Dictionary {value - 256}: {key}")

    return result


def lzw_decompress(input_codes):
    # Initialize the dictionary with single character strings as keys and their ascii values as values.
    dictionary = {i: chr(i) for i in range(256)}
    current_string = chr(input_codes[0])  # Start with a string consisting of the first input code.
    result = current_string  # The output is a string.

    for code in input_codes[1:]:
        print(f"Step: Current code = {code}")
        if code in dictionary:  # If the current code is in the dictionary,
            # Then its associated string is the current string.
            new_string = dictionary[code]
        else:  # If the current code is not in the dictionary (it must be the next available code),
            # Then its associated string is the current string followed by the first symbol of the current string.
            new_string = current_string + current_string[0]
        result += new_string  # Add the new string to the output string.
        print(f"Output: {new_string}")
        # Add a new entry to the dictionary for the current string followed by the first symbol of the new string.
        dictionary[len(dictionary)] = current_string + new_string[0]
        print(f"Add to the dictionary: {len(dictionary) - 1} -> {dictionary[len(dictionary) - 1]}")
        current_string = new_string  # Make the new string the current string.

    print("Final Dictionary:")
    for key, value in dictionary.items():
        print(f"{key} -> {value}")

    return result


#text = "kokosi_un_banani"
#compressed = lzw_compress(text)
#print("Compressed:", compressed)
compressed = [11, 15, 0, 11, 21, 27, 29, 15, 11, 1, 29, 36, 30, 35]
#compressed = [11 - 256, 15 - 256, 0 - 256, 11 - 256, 21 - 256, 27 - 256, 29 - 256, 15 - 256, 11 - 256, 1 - 256, 29 - 256, 36 - 256, 30 - 256, 35 - 256]

decompressed = lzw_decompress(compressed)
print("Decompressed:", decompressed)
