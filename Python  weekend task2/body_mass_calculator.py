print("BODY MASS CALCULATOR")

weight = float(input("""Enter  Number Of Your Weight:   
"""))
height = float(input("""Enter Number Of Your Height:   
"""))
  
body_mass_index = weight / (height * height)
print = ("body_mass_index is", body_mass_index  )

if body_mass_index < 18.5:
    print("Underweight")
if body_mass_index >= 18.5 and  body_mass_index <= 24.9:
    print ("Normal")
if body_mass_index >= 25   and  body_mass_index <= 29.9:
    print("Overweight")
if body_mass_index >=30:
    print("Obese")
