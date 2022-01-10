"""

This code prompts you to enter the classes you are taking, including the GPA
and credit hours 
Example:
classes = [("ENGL 1102",4.0,3),("CS 2050",2.5,3),("CS 1331",3.5,3),
           ("EAS 1601",4.0,4),("MATH 2550",2.5,2),("MUSI 1XX",4.0,1)]
           
"""
def findGPA():
    classes = []
    num = None
    
    while type(num) != int:
        try:
            num = int(input("How many classes are you taking? \n"))
            
        except:
            print("Please enter an integer. Thanks! \n")

    count = 1
    totalCredits = 0
    
    for num in range(0,num):
        string = None
        grade = None
        credit = None
        
        string = input("Enter the name of class " + str(count) + ": ")
        
        
        while type(grade) != float:
            try:
                grade = float(input("Enter the GPA you have in class " + str(count) +
                      ":  \n (Note: STEM classes have an extra .5 added for Zell Miller calculation) \n"))
            except:
                print("Please enter a float value for this! Ex. 3.0, 2.5, etc \n")

        
        while type(credit)!= int:
            try:
                credit = int(input("Enter the credit hours of class " + str(count) + ": "))
            except:
                print("Please enter an integer. Thanks! \n")


        newtup = (string,grade,credit)
        classes.append(newtup)
        count += 1
        totalCredits += credit
        
    
    print("You are taking a total of " + str(totalCredits) + " credit hours.")
    print("Here is a list of your classes! :)")
    print(classes)
        
    total = 0
    weight = 0
    for string, grade, credit in classes:
        weight += (grade * credit)
        total += credit
    
    print("Your weighted GPA calculation is a " + str(weight/total) + ".")

    if (weight/total) > 6.0:
        print("I uhh,, feel like ur cheating my dude.")
    elif (weight/total) >= 4.0:
        print("Way to go superstar! :D")
    elif (weight/total) >= 3.3:
        print("Hey! That meets Zell Miller. Great job! :)")
    elif (weight/total) >= 3.0:
        print("A B average! That keeps Hope :) Woohoo!!")
    elif (weight/total) >= 2.0:
        print("C's get degrees my dude. You got this! B)")
    elif (weight/total) < 2.0:
        print("Sorry bout that love. You can get em next time though! I believe in you :)")


    bet = input("Oh! Would you like to find your total GPA? Enter 'yes' if so. \n")

    if bet.lower() == "yes":
        ans = float(input("Betttt. So, what is your current GPA (you can look this up on DegreeWorks or GA Futures)? \n"))
        earlyCredits = float(input("And how many previous credit hours have you taken? Not including this semester ofc.\n"))
        new = (ans * earlyCredits) + weight
        newTotal = earlyCredits + total
        
        print("Aight, so your total GPA will be " + str(new/newTotal) + ".")
        
        if (new/newTotal) > 6.0:
            print("I uhh,, feel like ur cheating my dude.")
        elif (new/newTotal) >= 4.0:
            print("Way to go superstar! :D")
        elif (new/newTotal) >= 3.3:
            print("Hey! That meets Zell Miller. Great job! :)")
        elif (new/newTotal) >= 3.0:
            print("A B average! That keeps Hope :) Woohoo!!")
        elif (new/newTotal) >= 2.0:
            print("C's get degrees my dude. You got this! B)")
        elif (new/newTotal) < 2.0:
            print("Sorry bout that love. You can get em next time though! I believe in you :)")

    
    answer = input("Okee! Run again? Enter 'yes' if so. \n")
    if answer.lower() == "yes":
        findGPA()
    else:
        print("Okee!! Cya <3")
        return 

findGPA()
