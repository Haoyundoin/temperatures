"""This code converts temperatures between °F and °C"""

temperature = int(input("Please write the temperature"))
mode = input("Please indicate if it's in Fahrenheit or Celsius (F/C)?")

if mode == 'F':
    celsius = (temperature - 32) * 5/9
    print(celsius)
elif mode == 'C':
    fahrenheit = temperature * 9/5 + 32
    print(fahrenheit)
else:
    mode = input("ERROR: Please indicate if it's in Fahrenheit or Celsius (F/C)?")