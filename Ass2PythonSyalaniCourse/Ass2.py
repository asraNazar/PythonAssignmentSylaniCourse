#Write a program which takes 5 inputs from user for different subject’s
# marks, total it and generate mark sheet using grades ?

print("MARKSHEET")
mark1 = int(input());
mark2 = int(input());
mark3 = int(input());
mark4 = int(input());
mark5 = int(input());
sum = mark1 + mark2 + mark3 + mark4 + mark5;
average = sum / 5;
print(average)
if (average >= 91 and average <= 100):
    print("Your Grade is A+");
elif (average >= 81 and average <= 90):
    print("Your Grade is A");
elif (average >= 71 and average <= 80):
    print("Your Grade is B+");
elif (average >= 61 and average <= 70):
    print("Your Grade is B");
elif (average >= 51 and average <= 60):
    print("Your Grade is C+");
elif (average >= 41 and average <= 50):
    print("Your Grade is C");
elif (average >= 0 and average <= 40):
    print("Your Grade is F");
else:
    print("Strange Grade..!!")


# Write a program which take input from user and identify that the given
# number is even or odd?

a=int(input("Enter any number to check if it is even or odd"))
if a%2==0:
    print("The number is even")
print("The number is odd")

# Write a program which print the length of the list?
li=['a','b','c']
print("Length of list is: ",len(li))

# #Write a Python program to sum all the numeric items in a list?
li=[]
total=0
print("Enter list elements")
for i in range(4):
    i=int(input())
    li.append(i)
    total+=i
print("Total is ",total)

#Write a Python program to get the largest number from a numeric list.
li=[]
print("Enter list elements")
for i in range(4):
    i=int(input())
    li.append(i)
print("Maximum element is",max(li))

# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are
# less than 5.
l=[]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<5:
        l.append(i)
print(l)