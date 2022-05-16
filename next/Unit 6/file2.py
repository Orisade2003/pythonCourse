import file1


class BirthdayCard(file1.GreetingCard):
    def __init__(self, sender_age=0, recipient='Dana Ev', sender='Eyal Ch'):
        """
        :param sender_age: The age of the sender
        :type sender_age:int
        :param recipient: The name of the person receiving the greeting card
        :type recipient: str
        :param sender: The name of the person sending the greeting card
        :type sender: str
        The function sets the attributes of the instance
        The default values of the attributes are _sender_age = 0, _recipient='Dana Ev', _sender='Eyal Ch'
        """
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        """
        The function prints who the recipient of the greeting card is and who the sender is
        as well as the string 'Happy Birthday' and the age of the sender
       """
        super().greeting_msg()
        print("Happy Birthday")
        print("Sender Age: ", self._sender_age)
