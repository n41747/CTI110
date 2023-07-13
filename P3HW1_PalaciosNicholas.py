# I was supposed to put a comment here
# Palacios
# CTI-110



mod_1=float(input('Enter grade for Module 1: '))
mod_2=float(input('Enter grade for Module 2: '))
mod_3=float(input('Enter grade for Module 3: '))
mod_4=float(input('Enter grade for Module 4: '))
mod_5=float(input('Enter grade for Module 5: '))
mod_6=float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

lowest= min(grades)
highest= max(grades)
sum1= sum(grades)
average= sum(grades) / len(grades)

print("------Results------")
print("Lowest Grade:     ", lowest)
print("Highest Grade:     ", highest)
print("Sum Of Grade:     ", sum1)
print("Average  :     ", format(average,',.2f'))
print("-"*40)




if average >= 90:
    print('Your grade is: A')
else:
        if average >= 80:
         print('Your grade is: B')
        else:
            if average >= 70:
                print('Your grade is: C')
            else:
                if average >= 60:
                    print('Your grade is: F')





