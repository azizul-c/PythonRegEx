import re

def exercise_1():
    """
    Exercise 1: Find all digits in the string.
    """
    text = "I have 2 apples, 10 oranges, and 5 bananas."
    # Fill in the regex to find all digits in the text
    pattern = r"[0-9]+"
    result = re.findall(pattern, text) # findAll -- The list contains the matches in the order they are found.
    print("Exercise 1:", result)  # Expected Output: ['2', '10', '5']


def exercise_2():
    """
    Exercise 2: Find all words that start with 'a' or 'A'.
    """
    text = "Apples are amazing, but avocados are even better!"
    # Fill in the regex to find all words starting with 'a' or 'A'
    pattern = r"\AaA"
    result = re.findall(pattern, text)
    print("Exercise 2:", result)  # Expected Output: ['Apples', 'are', 'amazing', 'avocados', 'are']


def exercise_3():
    """
    Exercise 3: Find all email addresses in the text.
    """
    text = "You can reach out to john.doe@example.com or jane_doe123@my-email.org for more information."
    # Fill in the regex to find all email addresses
    pattern = r"[a-z0-9_.+-]+@[a-z0-9_.+-]+\.[a-z]+"
    result = re.findall(pattern, text)
    print("Exercise 3:", result)  # Expected Output: ['john.doe@example.com', 'jane_doe123@my-email.org']


def exercise_4():
    """
    Exercise 4: Replace all occurrences of multiple spaces with a single space.
    """
    text = "This   is    a    string with     irregular   spacing."
    # Fill in the regex to replace multiple spaces with a single space
    pattern = r"\s+" 
        # Note: I did it like this first, but the square brackets aren't really needed: r"[\s+]"
    result = re.sub(pattern, " ", text)
    print("Exercise 4:", result)  # Expected Output: "This is a string with irregular spacing."


def exercise_5():
    """
    Exercise 5: Validate if the given string is a valid phone number (format: XXX-XXX-XXXX).
    """
    phone_numbers = [
        "123-456-7890",  # Valid
        "123-45-7890",   # Invalid
        "987-654-3210",  # Valid
        "9876543210"     # Invalid
    ]
    
    # Fill in the regex to validate phone numbers in the format XXX-XXX-XXXX
    pattern = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
        # Alternate solution: r"\d{3}-\d{3}-\d{4}"
    
    for phone in phone_numbers:
        match = re.fullmatch(pattern, phone)
        if match:
            print(f"Exercise 5: {phone} is valid.")
        else:
            print(f"Exercise 5: {phone} is invalid.")


def main():
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()


if __name__ == "__main__":
    main()
