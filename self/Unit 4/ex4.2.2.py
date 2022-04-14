def isPoly():
    input_string = input("Enter a string")
    backwards_string = input_string[-1::-1]
    if backwards_string == input_string:
        print("OK")
    else:
        print("not")





if __name__ == "__main__":
    isPoly()