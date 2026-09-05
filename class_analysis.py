'''student class analysis program it accepts students names and marks and generates a class analysis'''
#function to calc grade
def calculate_grade(marks):
    if marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "C"
    elif marks>=50:
        return "D"
    else:
        return "F"
#function to enter student details
def enter_students():
    students=[]
    n=int(input("enter no of students :"))
    for i in range(n):
        print("\nstudent",i+1)
        name=input("enter name:")
        marks=float(input("enter marks :"))
        grade=calculate_grade(marks)

        students.append({"name" : name, "marks" : marks, "grade" : grade})
    return students

def generate_report(students):
    total=0
    for student in students:
        total = total + student["marks"]
        average = total/len(students)
        highest = students[0]
        lowest = students[0]
    for student in students:
        if student["marks"]>highest["marks"]:
            highest = student
        if student["marks"]<lowest["marks"]:
            lowest = student
    passed=0
    failed=0
    for student in students:
        if student["marks"]>=40:
            passed=passed + 1
        else:
            failed=failed + 1
    pass_percentage = (passed/len(students))*100
    print("\n============== CLASS REPORT ==============")
    print("\nName \tMarks \tGrade")
    for student in students:
        print(student["name"], "\t", student["marks"], "\t", student["grade"])
#display the overall class analysis
    print("\nClass Average:",round(average,2))
    print("Highest:",highest["name"])
    print("Lowest:",lowest["name"])
    print("number passed:",passed)
    print("number failed:",failed)
    print("pass percentage:",round(pass_percentage,2),"%")
    return average,highest,lowest,passed,failed,pass_percentage
#funtion to save the result in the txt file
def save_report(students,average,highest,lowest,passed,failed,pass_percentage):
    with open("class_report.txt","w") as file:
        file.write("========== CLASS REPORT ==========\n\n")
        file.write("Name\tMarks\tGrade\n")
        file.write("---------------------------------------\n")
        for student in students:
            file.write(student["name"]+"\t"+ str(student["marks"])+"\t"+student["grade"]+"\n")
        file.write("\nclass average:"+str(round(average,2)))
        file.write("\nhighest:"+highest["name"])
        file.write("\nlowest:"+lowest["name"])
        file.write("\nnumber passed:"+str(passed))
        file.write("\nnumber failed:"+str(failed))
        file.write("\npass percentage:"+str(round(pass_percentage,2)) + "%")
    print("\nreport saved successfully as class_report.txt")
def main():
    print("===== STUDENT CLASS ANALYSIS =====")
    students=enter_students()
    average,highest,lowest,passed,failed,pass_percentage = generate_report(students)
#ask whether the user wants to save the report
    choice=input("\nsave report to a text file? (yes/no):")
    if choice.lower()=="yes":
        save_report(students,average,highest,lowest,passed,failed,pass_percentage)
    print("\nprogram completed successfully")
#start the program
main()
        
    
    
    
                
                                
                                
        
    
