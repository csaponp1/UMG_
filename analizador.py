
# Import the necessary modules
import os
import tokenize

# Define a function to upload a file from a given path
def upload_file(path):
  # Check if the path is valid and the file is readable
  if os.path.isfile(path) and os.access(path, os.R_OK):
    # Open the file and return it as an object
    file = open(path, "r")
    return file
  else:
    # Raise an exception if the path is invalid or the file is not readable
    raise FileNotFoundError(f"File {path} does not exist or is not readable")

# Define a function to save a file to a given path
def save_file(file, path):
  # Check if the file is writable
  if os.access(path, os.W_OK):
    # Write the file content to the path
    with open(path, "w") as output:
      output.write(file.read())
  else:
    # Raise an exception if the file is not writable
    raise PermissionError(f"File {path} is not writable")

# Define a function to obtain tokens from a file object
def get_tokens(file):
  # Use the tokenize module to generate tokens from the file object
  tokens = tokenize.generate_tokens(file.readline)
  # Return a list of tokens
  return list(tokens)

# Define a function to classify tokens by their type
def classify_tokens(tokens):
  # Create an empty dictionary to store the token types and counts
  token_types = {}
  # Loop through the tokens
  for token in tokens:
    # Get the token type name from the tokenize module
    token_type = tokenize.tok_name[token.type]
    # Increment the count for the token type in the dictionary
    token_types[token_type] = token_types.get(token_type, 0) + 1
  # Return the dictionary of token types and counts
  return token_types

# Example usage
# Upload a file from a given path
file = upload_file("C:\Users\willy\Documents\python\ejercicio.py")
# Save a copy of the file to another path
save_file(file, "copy.py")
# Get the tokens from the file object
tokens = get_tokens(file)
# Classify the tokens by their type
token_types = classify_tokens(tokens)
# Print the token types and counts
print(token_types)
