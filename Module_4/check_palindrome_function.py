# Module 4.1 Intraduction to Python functions
# Module 4.2 Function arguments

# Program a function that takes one argument (string type), 
# returns a boolean value: True/False, 
# indicating whether the given text is a palindrome.
# 
def check_if_palidrome(text):
    """
    check if the one given argument is a palindrome,
    the argument is string typed,
    the function returns boolean True or False value
    """
    return text == text[::-1]

print(check_if_palidrome('civic'))
print(check_if_palidrome('madam'))
print(check_if_palidrome('mist'))
print(check_if_palidrome('radar'))
print(check_if_palidrome('noon'))
print(check_if_palidrome('hazard'))
print(check_if_palidrome('pip'))