import operator

def readstudentdetails():
    print()
    print("Enter the number of Students : ")
    numberofstudents = int(input())
    studentrecord = {}
    for no in range(0, numberofstudents):
        print("Enter the name of Students : ")
        name = input()
        print("Enter the mark of Students : ")
        marks = int(input())        
        studentrecord[name] = marks
    print()
    return studentrecord
    
def rankstudents(studentrecord):
    try:
        print()
        sortedmark = sorted(studentrecord.items(), key=operator.itemgetter(1), reverse = True)
        print(sortedmark)
        print("{} has secured 1st rank with the marks {}".format(sortedmark[0][0],sortedmark[0][1]))
        print("{} has secured 1st rank with the marks {}".format(sortedmark[1][0],sortedmark[1][1]))
        print("{} has secured 1st rank with the marks {}".format(sortedmark[2][0],sortedmark[2][1]))
        print()
        return sortedmark
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()
        
def rewardstudents(sortedmark,rewards):
    print()
    print("{} received the cash reward of $ {}".format(sortedmark[0][0],rewards[0]))
    print("{} received the cash reward of $ {}".format(sortedmark[1][0],rewards[1]))
    print("{} received the cash reward of $ {}".format(sortedmark[2][0],rewards[2]))
    print()

def appreciatestudents(sortedmark):
    print()
    for record in sortedmark:
        if record[1] >= 50:
            print("Conrats for scoring {} marks {}".format(record[1],record[0]))
        else:
            break
    print()    





studentrecord  = readstudentdetails()
sortedmark = rankstudents(studentrecord)
rewards = (300,200,100)
rewardstudents(sortedmark,rewards)
appreciatestudents(sortedmark)
