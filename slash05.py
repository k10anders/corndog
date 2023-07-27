def replace_backslash(string):
    return string.replace("\\", "/")

# Prompt the user to enter a file path with backslashes
original_string = input("Enter a file path with backslashes: ")

# Replace backslashes with forward slashes
new_string = replace_backslash(original_string)

# Display the modified file path
print("Modified file path:", new_string)

# Wait for user input before closing the console window
input("Press Enter to close the console window...")
