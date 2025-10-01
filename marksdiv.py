"""5. The marks obtain by a student in 5 different subjects are input
through keyboard. The student gets the division as per the following
rules:
Percentage above or equal to 60- first division
Percentage between 50 and 59- second division
Percentage between 40 and 49 – third division
Percentage below 40- fails. """


marks=int(input("enter the marks of student="))
if marks>=60:
    print("first division")
elif marks>50 and marks<59:
    print("second division")
elif marks>40 and marks<49:
    print("third division")
elif marks<40:
    print("fails")
