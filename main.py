# Print Hello World
print("Hello World")

# Define the height of the pyramid
height = 5

# Print star pyramid
for i in range(1, height + 1):
    # Print spaces
    print(" " * (height - i), end="")
    # Print stars
    print("*" * (2 * i - 1))
