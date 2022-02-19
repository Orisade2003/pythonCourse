def checkValidity():
    letter = input("Enter A Letter: ")
    if(len(letter) > 1 and not letter.isalpha()):
        print("E3")
    elif not letter.isalpha():
        print("E2")
    elif len(letter)>1:
        print("E1")
    else:
        print(letter.lower())

if __name__ == '_main__':
    checkValidity()