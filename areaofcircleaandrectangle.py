"""6. Write a program that has following menu:
Enter 1 to find the area of rectangle.
Enter 2 to find the area of circle.
Values for length and width of a rectangle and value of a radius of
circle will be entered through keyboard. """

radius=int(input("enter the radius="))
length=float(input("enter the length="))
width=float(input("enter the width="))
option=input("""select an option
1.area_of_circle
2.area_of_rectangle""")
if option=="1":
    print(3.14*radius)
elif option=="2":
    print(length*width)
else:
    print("no result")
