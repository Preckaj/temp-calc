def CelsiustoFahrenheit(x):
    return (x*(9/5))+32
def FahrenheitToCelsius(x):
    return (x-32)*(5/9)

def ConsoleText():
    while True:
        print("====Temperature  Calculator====")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        action = int(input("What do you pick? --> "))
        if action == 1:
            try:
                number = float(input("What temperature? --> "))
                result = CelsiustoFahrenheit(number)
                print(f"It is {result:2f}°F outside!")
            except ValueError:
                print("Invalid value, please enter a number.")
        elif action == 2:
            try:
                number = float(input("What temperature? --> "))
                result = FahrenheitToCelsius(number)
                print(f"It is {result:2f}°C outside!")
            except ValueError:
                print("Invalid value, please enter a number.")
        elif action == 3:
            exit()
        else:
            print("Invalid value, please enter a number.")