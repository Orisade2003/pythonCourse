import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        """
        :param arg: the username of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        The Function tells the User that there is an illegal character in their username
        """
        illegal_charcter = ''
        counter = 0
        for ch in self._arg:
            if not ch.isalnum() or  ch != '_':
                illegal_character = ch
            counter += 1
        params = (illegal_character, counter - 1)
        return 'Your Username contains an illegal character "%s" at %s ' %params

    def get_arg(self):
        """
        :return: The username
        :rtype: str
        """
        return self._arg


class UsernameTooShort(Exception):
    def __init__(self, arg):
        """
        :param arg: the username of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        The Function tells the User that there their username is too short
        """
        return "Your Username is too short since it contains less than 3 characters"

    def get_arg(self):
        """
        :return: The username
        :rtype: str
        """
        return self._arg


class UsernameTooLong(Exception):
    def __init__(self, arg):
        """
        :param arg: the username of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        return : The Function tells the User that there their username is too long
        :rtype:str
        """
        return "Your Username is too long as it contains more than 16 characters"

    def get_arg(self):
        """
        :return: The username
        :rtype: str
        """
        return self._arg


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        """
        :param arg: the password of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        return: The Function tells the User that there their password is missing one of the required characters
        :rtype:str
        """
        lowercase_counter = 0
        uppercase_counter = 0
        special_chars_counter = 0
        digits_counter = 0
        for char in self._arg:
            if 'a' <= char <= 'z':
                lowercase_counter += 1
            if 'A' <= char <= 'Z':
                uppercase_counter += 1
            if char in string.punctuation:
                special_chars_counter += 1
            if '0' <= char <= '9':
                digits_counter += 1
        missing_char = ''
        if uppercase_counter == 0:
            missing_char = "Uppercase"
        elif lowercase_counter == 0:
            missing_char = "Lowercase"
        elif digits_counter == 0:
            missing_char = "Digit"
        elif special_chars_counter == 0:
            missing_char = "Special"
        return "Your Password is missing one of the required characters (%s)" %missing_char

    def get_arg(self):
        """
        :return: The password
        :rtype: str
        """
        return self._arg


class PasswordTooShort(Exception):
    def __init__(self, arg):
        """
        :param arg: the password of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        return: The Function tells the User that there their password is too short
        :rtype:str
        "
        """
        return "Your Password is too short since it contains less than 8 characters"

    def get_arg(self):
        """
        :return: The password
        :rtype: str
        """
        return self._arg


class PasswordTooLong(Exception):
    def __init__(self, arg):
        """
        :param arg: the password of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        return: The Function tells the User that there their password is too Long
        :rtype:str
        "
        """
        return "Your Password is too short since it contains more than 40 characters"

    def get_arg(self):
        """
        :return: The password
        :rtype: str
        """
        return self._arg


def check_input2(username, password):
    """
    :param username: Username given by the user
    :type username: str
    :param password: Password given by the user
    :type password: str
    :return: True if the username is between 3 and 16 characters(inclusive) and includes only alphabetical letters
    , numbers and underscores, and the password is between 8 and 40 characters long(inclusive) and contains a lowercase letter,
    an uppercase letter, a number and a punctuation mark. THe function returns False otherwise
    """
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



def check_input(username, password):
    """
    :param username: Username given by the user
    :type username: str
    :param password: Password given by the user
    :type password: str
    :return: True if the username is between 3 and 16 characters(inclusive) and includes only alphabetical letters
    , numbers and underscores, and the password is between 8 and 40 characters long(inclusive) and contains a lowercase letter,
    an uppercase letter, a number and a punctuation mark. THe function returns False otherwise
    """
    username_check = username.replace("_", "")
    if not username_check.isalnum():
        raise UsernameContainsIllegalCharacter(username)
    if 3 > len(username):
        raise UsernameTooShort(username)
    if 17 <= len(username):
        raise UsernameTooLong(username)
    lowercase_counter = 0
    uppercase_counter = 0
    special_chars_counter = 0
    digits_counter = 0
    for char in password:
        if 'a' <= char <= 'z':
            lowercase_counter += 1
        if 'A' <= char <= 'Z':
            uppercase_counter += 1
        if char in string.punctuation:
            special_chars_counter += 1
        if '0' <= char <= '9':
            digits_counter += 1
    if lowercase_counter == 0 or uppercase_counter == 0 or special_chars_counter == 0 or digits_counter == 0:
        raise PasswordMissingCharacter(password)
    if 8 > len(password):
        raise PasswordTooShort(password)
    if 40 < len(password):
        raise PasswordTooLong
    print("OK")



def main():
    #check_input("1", "2")
   # check_input("0123456789ABCDEFG", "2")
   # check_input("A_a1.", "12345678")
   # check_input("A_1", "2")
   # check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    #check_input("A_1", "abcdefghijklmnop")
    #check_input("A_1", "ABCDEFGHIJLKMNOP")
    #check_input("A_1", "ABCDEFGhijklmnop")
    #check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == "__main__":
    main()
