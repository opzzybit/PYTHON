temperature = float(input("""Enter the number of temperature in Celsius: 
"""))
fahrenheit = (9 * temperature) / 5 + 32
temperature = temperature + 1
for temperature in range(5):
        if temperature > -273:
            print (f"the fahrenheit is {fahrenheit}")
        break
        if temperature < -273:
             print("impossible")
