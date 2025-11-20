import math #Importing math to use Pi in area calculation
print("Welcome to my Python program")
print("Hello user this is a 2-D shape area calculator")
shape = input("What shape is it(Square,  Rectangle, Triangle, Circle)").upper()
unit = input("What unit of measurement are you using?")
#calculating area of Rectangle using If, Elif, and Else staments to calculte area based on certain conditions
if shape == "RECTANGLE": 
    try:
        length = float(input("What is the length of the rectangle?"))
        width = float(input("What is the width of the rectangle?"))

    except ValueError:
        print("Please enter a valid number")
    
    area = length * width
    print(f"The reactangles area is: {area:.2f} {unit} squared")
#Calculating area of Square
elif shape == "SQUARE":
  try:
        side = float(input("What is the length of the rectangle?"))
  except ValueError:
        print("Please enter a valid number")
    
  area = side * side
  print(f"The area of the Square is: {area:.2f} {unit} squared")
#calculating area of Triangle
elif shape == "TRIANGLE":
    try:
        base = float(input("How long is the base of the Traingle?"))
        height = float(input("What is the Height of the Triangle?"))
    except:
        print("Please enter a valid number")
    area = (height * base) / 2
    print(f"The area of the Triangle is: {area} {unit}")
#Calculating area of cirlce
elif shape == "CIRCLE":
    try:
        radius = float(input("What is the radius of the circle(Half of the diameter)?"))
    except:
        print("Please enter a valid number")
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area} {unit} squared")
else:
    print("Check spelling or choose one of the 4 shapes from above.")