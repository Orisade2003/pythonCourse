import string


def check_input(username, password):
    is_username_legal = False
    is_password_legal = False
    capital_letter_counter = 0
    lowercase_counter = 0
    special_chars_counter = 0
    digits_counter = 0
    if 3 <= len(username) <= 16:
        username = username.replace("_", "")
        if username.isalnum():
            is_username_legal = True
    if 40 >= len(password) >= 8:
        for char in password:
            if 'a' <= char <= 'z':
                lowercase_counter += 1
            if 'A' <= char <= 'Z':
                capital_letter_counter += 1
            if char in string.punctuation:
                special_chars_counter += 1
            if '0' <= char <= '9':
                digits_counter += 1
        if capital_letter_counter > 0 and lowercase_counter > 0 and digits_counter > 0 and special_chars_counter > 0:
            is_password_legal = True
    if is_password_legal and is_username_legal:
        print("OK")


def main():
    check_input("A_32", "fskldfj4A.")

if __name__ == "__main__":
    main()

