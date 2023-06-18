def lzw_compress(input_string):
    # Initialize the dictionary with single character strings as keys and their ascii values as values.
    dictionary = dictionary = {'_': 0}
    dictionary.update({chr(i + 65): i + 1 for i in range(26)})
    print("Initial Dictionary:")
    for key, value in dictionary.items():
        print(f"Dictionary {value}: {key}")

    current_string = ""  # Start with an empty current string.
    result = []  # The output will be a list of codes.
    step = 1

    for symbol in input_string:
        print(f"\nStep {step}: Current string + symbol = {current_string + symbol}")
        if current_string + symbol in dictionary:  # If the current string followed by the current symbol is in the dictionary,
            current_string = current_string + symbol  # then make that the current string.
        else:  # If the current string followed by the current symbol is not in the dictionary,
            # Add a new entry to the dictionary for the current string followed by the current symbol.
            dictionary[current_string + symbol] = len(dictionary)
            # Output the code for the current string.
            result.append(dictionary[current_string])
            print(f"Output: {dictionary[current_string]}")
            print(f"Add to the dictionary: {len(dictionary) - 1}: {current_string + symbol}")
            current_string = symbol  # Start a new current string with the current symbol.
        step += 1

    # Output the code for the current string, if it is not empty.
    if current_string:
        result.append(dictionary[current_string])
        print(f"Output: {dictionary[current_string]}")

    print("\nFinal Dictionary:")
    for key, value in dictionary.items():
        if value >= 28:  # Print only the entries that we added during the compression.
            print(f"Dictionary {value - 28}: {key}")

    return result


def lzw_decompress(input_codes):
    # Initialize the dictionary with single character strings as keys and their ascii values as values.
    dictionary = {0: '_'}
    dictionary.update({i + 1: chr(i + 65) for i in range(26)})
    current_string = dictionary[input_codes[0]]  # Start with a string consisting of the first input code.
    result = current_string  # The output is a string.
    step = 1

    for code in input_codes[1:]:
        print(f"\nStep {step}: Current code = {code}")
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
        print(f"Add to the dictionary: {len(dictionary) - 27 - 1}: {current_string + new_string[0]}")

        current_string = new_string  # Make the new string the current string.
        step += 1

    print("\nFinal Dictionary:")
    for key, value in dictionary.items():
        if key >= 27:  # Print only the entries that we added during the decompression.
            print(f"Dictionary {key - 27}: {value}")

    return result


#text = "COCOA_AND_BANANAS"
#compressed = lzw_compress(text)
#print("Compressed:", compressed)
#compressed = [3, 15, 27, 1, 0, 1, 14, 4, 0, 2, 32, 32, 1, 19]
compressed = [11, 15, 0, 11, 21, 27, 29, 15, 11, 1, 29, 36, 30, 35]
decompressed = lzw_decompress(compressed)
print("Decompressed:", decompressed)
