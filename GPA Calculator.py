"""
Given a list of tuples, (class(str), grade(float), creditHours(int), find
the total weighted gpa
"""

#Total is grade times credit? return total

classes = [("ENGL 1102",4.0,3),("CS 2050",2.5,3),("CS 1331",2.5,3),
           ("EAS 1601",4.0,4),("MATH 2550",2.5,2),("MUSI 1XX",4.0,1)]

def findGPA(classes):
        
    total = 0
    weight = 0
    for string, grade, credit in classes:
        weight += (grade * credit)
        total += credit
    
    return weight/total

findGPA([("ENGL 1102",4.0,3),("CS 2050",3.5,3),("CS 1331",3.5,3),("EAS 1601",4.0,4),("MATH 2550",3.5,2),("MUSI 1XX",4.0,1)])
