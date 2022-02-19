def convertTemp():
    temperature = input("Insert the temperature you would like to convert")
    if temperature[-1] == 'F':
        c_temperature = temperature[:len(temperature)-1]
        c_temperature = float(c_temperature)
        c_temperature = (5 * c_temperature-160)/9
        print("Tempreture is: " +str(c_temperature) + "C")
    else:
        f_temperature = temperature[:len(temperature) - 1]
        f_temperature = float(f_temperature)
        f_temperature = (9*f_temperature + (32*5))/5
        print("Temperature is: " + str(f_temperature) + "F")


if __name__ == "__main__":
    convertTemp()