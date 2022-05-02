class GreetingCard:

    def __init__(self, recipient='Dana Ev', sender='Eyal Ch'):
        """
        :param recipient: The name of the person receiving the greeting card
        :type recipient: str
        :param sender: The name of the person sending the greeting card
        :type sender: str
        The function sets the attributes of the instance
        The default values of the attributes are recipient='Dana Ev', sender='Eyal Ch'
        """
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        """
        The function prints who the recipient of the greeting card is and who the sender is
        """
        params = (self._recipient, self._sender)
        print("Recipient: %s    Sender: %s" % params)


def main():
    greeting_card = GreetingCard()
    greeting_card.greeting_msg()


if __name__ == "__main__":
    main()
