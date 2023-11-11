# Function to create a pyramid of numbers from 1 to 20
def pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")
        
        # Print increasing numbers
        for k in range(1, i + 1):
            print(k, end=" ")
        
        # Print decreasing numbers
        for l in range(i - 1, 0, -1):
            print(l, end=" ")
        
        # Move to the next line after completing each row
        print()

# Set the value of n (the number of rows in the pyramid)
n = 20
pyramid(n)
