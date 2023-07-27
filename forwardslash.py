def replace_forward_slash(string):
    return string.replace("/", "\\")

# Prompt the user to enter a file path with forward slashes
original_string = input("Enter a file path with forward slashes: ")

# Replace forward slashes with backslashes
new_string = replace_forward_slash(original_string)

# Display the modified file path
print("Modified file path:", new_string)

# Wait for user input before closing the console window
input("Press Enter to close the console window...")
