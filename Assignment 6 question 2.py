def is_palindrome(string):
    string = string.replace(" ", "").lower() # remove spaces and convert to lowercase
    return string == string[::-1]

print(is_palindrome("Madam")) # True
print(is_palindrome("nurses run")) # False
