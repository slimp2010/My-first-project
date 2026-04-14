class Employee:
    name = str(input("What's your name? "))
    age = int(input("How old are you: "))
    points = int(input("How many points did you score? "))

emp = Employee

print("your name is",emp.name)
print("you're:", emp.age)
print("You did",emp.points)

if emp.points >= 17:
    print("you've completed your work")
else:
    print("you need to work!")
