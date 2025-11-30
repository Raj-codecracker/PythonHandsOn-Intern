import string

print("=== PASSWORD STRENGTH CHECKER ===")

# Function to check strength
def checkStrength(pw):
    length = len(pw)
    lcase = any(c.islower() for c in pw)
    ucase = any(c.isupper() for c in pw)
    digit = any(c.isdigit() for c in pw)
    symbol = any(c in string.punctuation for c in pw)

    # Strong password rule
    if length >= 12 and lcase and ucase and digit and symbol:
        return "Strong"

    # Medium password rule
    elif length >= 8 and (lcase or ucase) and digit:
        return "Medium"

    # Otherwise weak
    else:
        return "Weak"

# Run 10 times
count = 0
while count < 10:
    password = input("Enter your password: ")
    strength = checkStrength(password)
    print("Password Strength Level:", strength, "\n")
    count += 1
