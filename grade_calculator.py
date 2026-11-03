name = input("Enter student name: ")
math = float(input("Enter Math mark: "))
english = float(input("Enter English mark: "))
python = float(input("Enter Python mark: "))

if math < 0 or math > 100 or english < 0 or english > 100 or python < 0 or python > 100:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
else:
    average = (math + english + python) / 3

    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f"Student Name: {name}")
    print(f"average Marks: {average:.2f}")
    print(f"Grade: {grade}")
