# program to remove all vowels in a string
main_string = ("Guvi Geeks Network Private Limited")

# using if condition to remove all the vowels
if "a" in main_string: 
    main_string = main_string.replace('a', '')
if "e" in main_string:
    main_string = main_string.replace('e' , '')
if "i" in main_string:
    main_string = main_string.replace('i' , '')
if "o" in main_string:
    main_string = main_string.replace('o' , '')
if "u" in main_string:
    main_string = main_string.replace('u' , '')

# print the main_string   
print(main_string)
    