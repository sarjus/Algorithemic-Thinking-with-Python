"""
  This program takes a user's first and last name, concatenates them with a space in between,
  prints the full concatenated name, and then extracts and prints the last name using string slicing.
  Example:
  If the first name is "John" and the last name is "Doe", the function will print:
  - Concatenated string: John Doe
  - Sub-string (last name): Doe
  Author: Sarju S
  Date: 08-10-2024
  """
# Define the first and last names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate the first and last name with a space
full_name = first_name + " " + last_name

# Print the concatenated string
print(f"Concatenated string: {full_name}")

# Access and print the sub-string (last name only)
length_of_first_name=len(first_name)
last_name_substring = full_name[length_of_first_name+ 1:]
print(f"Sub-string (last name): {last_name_substring}")