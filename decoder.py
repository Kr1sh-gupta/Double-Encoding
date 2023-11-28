import urllib.parse


def double_encode(text):
    # First encode the input string once
    encoded_once = urllib.parse.quote(text)

    # Then encode it again to get the fully encoded result
    fully_encoded = urllib.parse.quote(encoded_once)

    return fully_encoded


# Get input from the user
input_string = input("Enter a string to double encode: ")

# Double encode the input string
double_encoded_string = double_encode(input_string)

# Print the double-encoded string
print("Double-encoded String:", double_encoded_string)
