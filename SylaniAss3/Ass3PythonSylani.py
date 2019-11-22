# Make a calculator using Python with addition , subtraction , multiplication ,
# division and power.

print("\t\tCALCULATOR")
num1 = int(input("Enter number 1st\n"))
op = input("Enter operation to  perform: \n+\n-\n*\n/\n^\n")
if op=='+':
    num2 = int(input("Enter number 2nd: \n"))
    res=num1+num2
    print("Result of operation: ",res)
elif op=='-':
    num2 = int(input("Enter number 2nd\n"))
    res=num1-num2
    print("Result of operation: ",res)
elif op=='*':
    num2 = int(input("Enter number 2nd\n"))
    res=num1*num2
    print("Result of operation: ",res)
elif op=='/':
    num2 = int(input("Enter number 2nd\n"))
    res=num1//num2
    print("Result of operation: ",res)
elif op=='^':
    num2 = int(input("raised to the power?\n"))
    res=num1**num2
    print("Result of operation: ",res)
else:
    print("Enter correct operator: ")

#Write a program to check if there is any numeric value in list using for loop
a=['a',3,4,'b','f','%','@']
new_list=[]
for n in a:
    if n.isnumeric():
        print(n)

#Write a Python script to add a key to a dictionary
mydictionary={"First name":" Asra ",
              "Last Name": " Nazar",
              "Qualification": " BS-CS"}
mydictionary["Gender"]= " Female"
for i in mydictionary.values():
    print(i)

# #Write a Python program to sum all the numeric items in a dictionary
myNumDict={"Number 1":3,
               "Number 2":5,
               "Number 3":36}
sum=0
for j in myNumDict.values():
    sum = sum + j
print("Sum of numeric values is: ",sum)

#Write a program to identify duplicate values from list
my_list = [20,30,20,30,40,50,15,11,20,40,50,15]
my_list.sort()
for i in range (len (my_list)-1):
 	if my_list[i] == my_list[i+1]:
            print ("Duplicates are:\n ",my_list[i])

#Write a Python script to check if a given key already exists in a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)

