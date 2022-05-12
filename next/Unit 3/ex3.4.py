import string


class UsernameContainsIllegalCharacter(Exception):
    """Class used to represent an exception for when the username contains an illegal character"""

    def __init__(self, arg):
        """
        The function inits an instance of the UsernameContainsIllegalCharacter exception
        :param arg: the username of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        The Function tells the User that there is an illegal character in their username
        """
        illegal_character = ''
        counter = 0
        for ch in self._arg:
            if not ch.isalnum() or ch != '_':
                illegal_character = ch
            counter += 1
        params = (illegal_character, counter - 1)
        return 'Your Username contains an illegal character "%s" at %s ' % params

    def get_arg(self):
        """
        The function returns the username
        :return: The username
        :rtype: str
        """
        return self._arg


class UsernameTooShort(Exception):
    """Class used to represent an exception for when the username is too short"""

    def __init__(self, arg):
        """
        The function inits an instance of the UsernameTooShort exception
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
        The function returns the username
        :return: The username
        :rtype: str
        """
        return self._arg


class UsernameTooLong(Exception):
    """Class used to represent an exception for when the username is too long"""

    def __init__(self, arg):
        """
        The function inits an instance of the UsernameTooLong exception
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
        The function retruns the username
        :return: The username
        :rtype: str
        """
        return self._arg


class PasswordMissingCharacter(Exception):
    """Class used to represent an exception for when the passwords is missing a mandatory character"""

    def __init__(self, arg):
        """
        The function inits an instance of the PasswordMissingCharacter exception
        :param arg: the password of the user
        :type arg: str
        """
        self._arg = arg

    def __str__(self):
        """
        return: The Function tells the User that there their password is missing one of the required characters
        :rtype:str
        """
        return "Your Password is missing a character"

    def get_arg(self):
        """
        The function returns the password
        :return: The password
        :rtype: str
        """
        return self._arg


class PasswordTooShort(Exception):
    """Class used to represent an exception for when the password is too short"""

    def __init__(self, arg):
        """
        The function inits an instance of the PasswordTooShort exception
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
        The function returns the passwords
        :return: The password
        :rtype: str
        """
        return self._arg


class PasswordsMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + '(Lowercase)'


class PasswordsMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + '(Uppercase)'


class PasswordsMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + '(Digit)'


class PasswordsMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + '(Special)'


class PasswordTooLong(Exception):
    """Class used to represent an exception for when the password is too long"""

    def __init__(self, arg):
        """
        The function inits an instance of the PasswordTooLong exception
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
        The function returns the password
        :return: The password
        :rtype: str
        """
        return self._arg


def check_input2(username, password):
    """
    The function prints 'OK' if the password and username are legal
    :param username: Username given by the user
    :type username: str
    :param password: Password given by the user
    :type password: str
    :return: True if the username is between 3 and 16 characters(inclusive) and includes only alphabetical letters
    , numbers and underscores, and the password is between 8 and 40 characters long(inclusive) and contains a lowercase
     letter,an uppercase letter, a number and a punctuation mark. THe function returns False otherwise
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
    , numbers and underscores, and the password is between 8 and 40 characters long(inclusive) and contains a lowercase
     letter, an uppercase letter, a number and a punctuation mark. THe function returns False otherwise
     :raises: UsernameContainsIllegalCharacter if the username contains an illegal character
     :raises: UsernameTooLong if the username is longer than 16 characters
     :raises UsernameTooShort if the username is shorter than 3 characters
     :raises PasswordTooLong if the passwords is longer than 40 characters
     :raises PasswordTooShort if the passwords is shorter than 8 characters
     :raises PasswordMissingCharacter if the passwords doesn't contain one of the following: a number, an uppercase letter, a lowercase letter or a special character

    """
    username_check = username.replace("_", "")
    if not username_check.isalnum():
        raise UsernameContainsIllegalCharacter(username)
    if 3 > len(username):
        raise UsernameTooShort(username)
    if 17 <= len(username):
        raise UsernameTooLong(username)
    if not any(ch.isupper() for ch in password):
        raise PasswordsMissingUppercase(password)
    if not any(ch.islower() for ch in password):
        raise PasswordsMissingLowercase(password)
    if not any(ch.isdigit() for ch in password):
        raise PasswordsMissingDigit(password)
    if not any(ch in string.punctuation for ch in password):
        raise PasswordsMissingSpecial(password)
    if 8 > len(password):
        raise PasswordTooShort(password)
    if 40 < len(password):
        raise PasswordTooLong(password)
    print('OK')


def main():
    # check_input("1", "2")
    # check_input("0123456789ABCDEFG", "2")
    # check_input("A_a1.", "12345678")
    # check_input("A_1", "2")
    # check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    # check_input("A_1", "abcdefghijklmnop")
    # check_input("A_1", "ABCDEFGHIJLKMNOP")
    # check_input("A_1", "ABCDEFGhijklmnop")
    # check_input("A_1", "4BCD3F6h1jk1mn0p")
    # check_input("A_1", "4BCD3F6.1jk1mn0p")

    invalid_credentials = True
    while invalid_credentials:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        try:
            check_input(username, password)
        except Exception as e:
            print(e)
        else:
            invalid_credentials = False


if __name__ == "__main__":
    main()
