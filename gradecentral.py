#import os;
#clear = lambda : os.system('clear') 
from statistics import mean as m

admins = {'Python':'Pass123@','user2':'pass2'}
studentDict = {}

def enterGrades():
    name = input('Student name: ')
    grade = input('Grade: ')
    if name in studentDict:
        print('Adding Grade...')
        studentDict[name].append(float(grade))
    else:
        #to do append above, must be a LIST [] and not just a float (or face the "AttributeError: 'float' object has no attribute 'append'")
        studentDict[name] = [float(grade)] 
    print(studentDict)

def removeStudent():
    name = input('Student to remove: ')
    if name in studentDict:
        print('Removing Student...')
        del studentDict[name]
    else:
        print('Student ', name, ' does not exists')
    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print (eachStudent,' has an avare grade of ', avgGrade)

        
login = input('Username: ');
passw = input('Password: ');

if login in admins:
    if admins[login] == passw:
        print('Welcome, ',login);
        ok = True;
        while (ok):
            print ('Welcome to Grade Central')
            print ('[1] - Enter Grades');
            print ('[2] - Remove Student');
            print ('[3] - Student Average Grades');
            print ('[4] - Exit');
            option = input('Choose your option:');
            if (option == '4'):
                ok = False;
            elif (option == '1'):
                enterGrades();
            elif (option == '2'):
                removeStudent();
            elif (option == '3'):
                studentAVGs();
            input();
    else:
        print('Invalid password.');
else:
    print('Invalid login.');
