import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    while True:

        password = ""
        for _ in range(length):
            password += secrets.choice(all_chars)

        constraints = [
            (nums, r"\d"),
            (special_chars, rf"[{symbols}]"),
            (uppercase, r"[A-Z]"),
            (lowercase, r"[a-z]"),
        ]

        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    return password


def main():
    password = generate_password()
    print("Generated Password:", password)


if __name__ == "__main__":
    main()
