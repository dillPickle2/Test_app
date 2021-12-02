def fahrenheit_from(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)
    return str(fahrenheit)

celsius = input("Enter celsius calue: ")
print(fahrenheit_from(celsius))
