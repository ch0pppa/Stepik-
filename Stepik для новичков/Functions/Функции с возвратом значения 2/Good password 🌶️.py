def is_password_good(password):
    """Checks if a password meets certain criteria."""

    if len(password) < 8:
        return False

    has_capital_letter = False
    has_lowercase_letter = False
    has_digit = False

    for char in password:
        if char.islower():  # Check for Cyrillic characters (inclusive of upper and lowercase)
            has_lowercase_letter = True
        elif char.isupper():  # Check for Cyrillic characters (inclusive of upper and lowercase)
            has_capital_letter = True
        elif char.isdigit():  #Check for digits
            has_digit = True

    return has_capital_letter and has_lowercase_letter and  has_digit  # Password is good if it has either Cyrillic or a digit


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))