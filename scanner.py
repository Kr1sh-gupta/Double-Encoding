import urllib.parse


def is_double_encoded(text):
    # Decode the input string
    decoded_once = urllib.parse.unquote(text)
    decoded_twice = urllib.parse.unquote(decoded_once)

    # Check if the decoded string is different from the original
    return decoded_twice != text


# Get input from the user
input_string = input("Enter a string to check for double encoding: ")

# Check if double encoding exists
if is_double_encoded(input_string):
    print("Double encoding detected!")
else:
    print("No double encoding detected.")
