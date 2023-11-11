# program to calculate number of unique characters in a string
def unique_characters(input_string):
    # Use a set to store unique characters
    unique_chars = set()

    # Iterate through the string and add each character to the set
    for char in input_string:
        unique_chars.add(char)

    # Return the number of unique characters
    return len(unique_chars)


input_str = input("Enter the string:")
result = unique_characters(input_str)
print(f"The number of unique characters in '{input_str}' is: {result}")
