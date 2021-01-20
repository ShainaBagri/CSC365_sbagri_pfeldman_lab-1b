import pandas as pd

# Works with 1 teacher per classroom; breaks with multiple teachers
def lastNameSearch(df_students, df_teachers, lastName):
    #teacherLastNames = []
    #teacherFirstNames = []
    new_df = df_students.loc[df_students['StLastName'] == lastName,
        ['StLastName', 'StFirstName', 'Grade', 'Classroom']]
    if new_df.empty:
        print("No student with this last name exists")
    else:
        new_df['TLastName'] = None
        new_df['TFirstName'] = None
        for key, data in new_df.items():
            if key=='Classroom':
                classNums = data
        for i in range(len(classNums)):
            teachers = df_teachers.loc[df_teachers['Classroom']==classNums.iat[i]]
            teacherLastNames = []
            teacherFirstNames = []
            for lastName in teachers['TLastName']:
                teacherLastNames.append(lastName)
            for firstName in teachers['TFirstName']:
                teacherFirstNames.append(firstName)
            print(teacherLastNames)
            new_df.at[new_df.index[i],'TLastName'] = teacherLastNames
            new_df.at[new_df.index[i],'TFirstName'] = teacherFirstNames
        print(new_df)

def lastNameBusSearch(df, lastName):
    new_df = df.loc[df['StLastName'] == lastName, 
        ['StLastName', 'StFirstName', 'Bus']]
    if new_df.empty:
        print("No student with this last name exists")
    else:
        print(new_df)

def teacherSearch(df_students, df_teachers, TLName):
    classroom = df_teachers.loc[df_teachers['TLastName']==TLName, 'Classroom'].iat[0]
    new_df = df_students.loc[df_students['Classroom'] == classroom, ['StLastName', 'StFirstName']]
    if new_df.empty:
        print("No teacher with this last name exists")
    else:
        print(new_df)

def busSearch(df, busNum):
    new_df = df.loc[df['Bus'] == busNum,
        ['StLastName', 'StFirstName', 'Grade', 'Classroom']]
    if new_df.empty:
        print("Bus route not found")
    else:
        print(new_df)

def gradeSearch(df, grade):
    new_df = df.loc[df['Grade'] == grade,
        ['StLastName', 'StFirstName']]
    if new_df.empty:
        print("No students in this grade")
    else:
        print(new_df)


def avgGPA(df, grade):
    new_df = df.loc[df['Grade'] == grade]
    if(new_df.empty):
        print("No students in this grade")
    else:
        print("Grade \tAverage GPA")
        print(grade, " \t", new_df["GPA"].mean())

def lowestGPA(df_students, df_teachers, grade):
    new_df = df_students.loc[df_students['Grade'] == grade,
        ['StLastName', 'StFirstName', 'GPA', 'Bus', 'Classroom']]
    if(new_df.empty):
        print("No students in this grade")
    else:
        minGPA = new_df["GPA"].min()
        student = new_df.loc[new_df['GPA'] == minGPA]
        classroom = student['Classroom'].iat[0]
        student = student.loc[:, ['StLastName', 'StFirstName', 'GPA', 'Bus']]
        teacher = df_teachers.loc[df_teachers['Classroom'] == classroom, ['TLastName', 'TFirstName']]
        student['TLastName'] = teacher['TLastName'].iat[0]
        student['TFirstName'] = teacher['TFirstName'].iat[0]
        print(student)

def highestGPA(df_students, df_teachers, grade):
    new_df = df_students.loc[df_students['Grade'] == grade,
        ['StLastName', 'StFirstName', 'GPA', 'Bus', 'Classroom']]
    if(new_df.empty):
        print("No students in this grade")
    else:
        maxGPA = new_df["GPA"].max()
        student = new_df.loc[new_df['GPA'] == maxGPA]
        classroom = student['Classroom'].iat[0]
        student = student.loc[:, ['StLastName', 'StFirstName', 'GPA', 'Bus']]
        teacher = df_teachers.loc[df_teachers['Classroom'] == classroom, ['TLastName', 'TFirstName']]
        student['TLastName'] = teacher['TLastName'].iat[0]
        student['TFirstName'] = teacher['TFirstName'].iat[0]
        print(student)

def numStudents(df):
    print("0: ", len(df[df['Grade'] == 0]))
    print("1: ", len(df[df['Grade'] == 1]))
    print("2: ", len(df[df['Grade'] == 2]))
    print("3: ", len(df[df['Grade'] == 3]))
    print("4: ", len(df[df['Grade'] == 4]))
    print("5: ", len(df[df['Grade'] == 5]))
    print("6: ", len(df[df['Grade'] == 6]))

#NR1
def classNumStudentSearch(df_students, classNum):
    new_df = df_students.loc[df_students['Classroom'] == classNum, ['StLastName', 'StFirstName']]
    if new_df.empty:
        print("Classroom not found")
    else:
        print(new_df)

#NR2
def classNumTeacherSearch(df_teachers, classNum):
    new_df = df_teachers.loc[df_teachers['Classroom'] == classNum, ['TLastName', 'TFirstName']]
    if new_df.empty:
        print("Classroom not found")
    else:
        print(new_df)

#NR3   
def teacherByGradeSearch(df_students, df_teachers, grade):
    new_df = df_students.loc[df_students['Grade']==grade, ['Classroom']]
    if new_df.empty:
        print("No teachers in this grade")
    else:
        for i in range(len(new_df.index)):
            teachers = df_teachers.loc[df_teachers['Classroom']==new_df.iloc[i]['Classroom'], ['TLastName', 'TFirstName']]
        print(teachers)

#NR4
def enrollmentByClass(df_students):
    classes = df_students['Classroom'].unique()
    classes.sort()
    for classroom in classes:
        new_df = df_students.loc[df_students['Classroom'] == classroom, ['Classroom', 'StLastName', 'StFirstName']]
        num = new_df['StLastName'].value_counts().sum()
        print(classroom, " ", num)

#NR5
def analyzeData(df_students, df_teachers):
    print(df_students)

def main():
    try:
        df_students = pd.read_csv("list.txt", header=None, names=['StLastName', 'StFirstName', 
            'Grade', 'Classroom', 'Bus', 'GPA'])
        df_teachers = pd.read_csv("teachers.txt", header=None, names=['TLastName', 'TFirstName',
            'Classroom'])
    except IOError as e:
        print(e)
        exit()

    quit = False
    while not quit:
        command = str(input("Type your command: "))
        split = command.split()

        if len(split) == 1:
            if split[0]!="I" and split[0]!="Info" and split[0]!="Q" and split[0]!="Quit" and split[0]!="E" and split[0]!="Enrollment":
                continue

        if split[0]=="S:" or split[0]=="Student:":
            lastName = split[1].upper()
            if len(split) != 3:
                lastNameSearch(df_students, df_teachers, lastName)
            elif len(split) == 3 and (split[2] == "B" or split[2] == "Bus"):
                lastNameBusSearch(df_students, lastName)
            else:
                continue
 
        elif split[0]=="Teacher:" or split[0]=="T:":
            lastName = split[1].upper()
            teacherSearch(df_students, df_teachers, lastName)
 
        elif split[0]=="B:" or split[0]=="Bus:":
            number = int(split[1])
            busSearch(df_students, number)
 
        elif split[0]=="Grade:" or split[0]=="G:":
            number = int(split[1])
            if split[2]=="Student" or split[2]=="S":
                gradeSearch(df_students, number)
            elif split[2]=="Teacher" or split[2]=="T":
                teacherByGradeSearch(df_students, df_teachers, number)
            elif split[2]=="High" or split[2]=="H":
                highestGPA(df_students, df_teachers, number)
            elif split[2]=="Low" or split[2]=="L":
                lowestGPA(df_students, df_teachers, number)
            else:
                continue
 
        elif split[0]=="Classroom:" or split[0]=="C:":
            number = int(split[1])
            if split[2]=="Student" or split[2]=="S":
                classNumStudentSearch(df_students, number)
            elif split[2]=="Teacher" or split[2]=="T":
                classNumTeacherSearch(df_teachers, number)
        
        elif split[0]=="A:" or split[0]=="Average:":
            number = int(split[1])
            avgGPA(df_students, number)

        elif split[0]=="E" or split[0]=="Enrollment":
            enrollmentByClass(df_students)
 
        elif split[0]=="I" or split[0]=="Info":
            numStudents(df_students)
 
        elif split[0]=="Q" or split[0]=="Quit":
            quit = True
 
        else:
            continue
 
 
if __name__ == "__main__":
    main()