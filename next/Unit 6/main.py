import file1
import file2


def main():
    greeting_card = file1.GreetingCard()
    birthday_card = file2.BirthdayCard(20)
    greeting_card.greeting_msg()
    birthday_card.greeting_msg()


if __name__ == "__main__":
    main()
