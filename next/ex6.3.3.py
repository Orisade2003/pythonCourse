import pyttsx3


def text_to_speech(text):
    """
    :param text: tex given to the function
    :type text:str
    The function uses the pyttsx3 package to read out loud the content of text
    """
    speech = pyttsx3.init()
    speech.say(text)
    speech.runAndWait()


def main():
    text = "first time i'm using a package in next.py course "
    text_to_speech(text)


if __name__ == "__main__":
    main()
