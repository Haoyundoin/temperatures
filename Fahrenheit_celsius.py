"""This code converts temperatures between °F and °C"""


import sys

temperature = int(sys.argv[2])
mode = sys.argv[1]

# temperature = int(input("Please write the temperature"))
# mode = input("Please indicate if it's in Fahrenheit or Celsius (F/C)?")

if len(sys.argv) != 3:
    print("""Usage: 
        python Fahrenheit_celsius.py (F,C) temp

    prints temps in the other unit at 2 decimal places""")
    sys.exit(1)

if mode == 'F':
    celsius = (temperature - 32) * 5/9
    print(f"{celsius:.3}°C")
elif mode == 'C':
    fahrenheit = temperature * 9/5 + 32
    print(round(fahrenheit, 2), "°F")
else:
    mode = input("ERROR: Please indicate if it's in Fahrenheit or Celsius (F/C)?")