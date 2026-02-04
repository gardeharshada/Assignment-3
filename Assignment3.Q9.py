# Input 5 subject marks from user and display grade(eg.First class, Second class...)
total = 0
for i in range(1,6):
    marks = float(input(f"Enter marks for subject {i}:"))
    total += marks

    percentage = total / 5
    print("Percentage=", percentage)
    
    if percentage >= 75:
        print("Grade: First class with Distinction" )
    elif percentage >= 60:
        print("Grade: First class")  

    elif percentage >= 50:
        print("Grade: Second class")
    elif percentage >= 35:
        print("Grade: Pass class")  
    else:
        print("Grade: Fail")      

