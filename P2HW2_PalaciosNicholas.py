#CTI-110
#P2HW2 - List
#Nicholas Palacios
#6/22
#

grade_list=[]

num1=float(input("Enter a grade for Module 1: "))
grade_list.append(num1)
num2=float(input("Enter a grade for Module 2: "))
grade_list.append(num2)
num3=float(input("Enter a grade for Module 3: "))
grade_list.append(num3)
num4=float(input("Enter a grade for Module 4: "))
grade_list.append(num4)
num5=float(input("Enter a grade for Module 5: "))
grade_list.append(num5)
num6=float(input("Enter a grade for Module 6: "))
grade_list.append(num6)
lowest= min(grade_list)
highest= max(grade_list)
sum1= sum(grade_list)
average= sum(grade_list) / len(grade_list)

print("------Results------")
print("Lowest Grade:     ", lowest)
print("Highest Grade:     ", highest)
print("Sum Of Grade:     ", sum1)
print("Average  :     ", format(average,',.2f'))
print("-"*40)




