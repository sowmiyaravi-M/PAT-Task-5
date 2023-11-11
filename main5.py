# program to find a string if it is palindrome or otherwise it is false
string = ("malayalam")

# to reverse the string
reversed_string = string[::-1]
print(reversed_string)

# checking it is palindrome using if-else condition
if string == reversed_string:
    print("Given string is palindrome")
else:
    print("Not a palindrome")