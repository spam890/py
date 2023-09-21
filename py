1A
# Input marks for three tests
marks1 = float(input("Enter test 1 marks: "))
marks2 = float(input("Enter test 2 marks: "))
marks3 = float(input("Enter test 3 marks: "))

# Calculate the average of the best two test marks
total_marks = marks1 + marks2 + marks3
minimum_mark = min(marks1, marks2, marks3)
best_two_sum = total_marks - minimum_mark
average_best_two = best_two_sum / 2

# Display the average of the best two test marks
print("Average of best two test marks: {:.2f}".format(average_best_two))

1B
val = int(input("Enter a value : "))
str_val = str(val)
if str_val == str_val[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
for i in range(10):
    if str_val.count(str(i)) > 0:
        print(str(i),"appears", str_val.count(str(i)), "times");

2A
def fn(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn(n-1) + fn(n-2)

num = int(input("Enter a number : "))

if num > 0:
    print("fn(", num, ") = ",fn(num) , sep ="")
else:
    print("Error in input")

2B
def bin2Dec(val):
    rev=val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
        i += 1
    
    return dec

def oct2Hex(val):
    rev=val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8**i
        i += 1
    list=[]
    while dec != 0:
        list.append(dec%16)
        dec = dec // 16
        
    nl=[]
    for elem in list[::-1]:
        if elem <= 9:
            nl.append(str(elem))
        else:
            nl.append(chr(ord('A') + (elem -10)))
    hex = "".join(nl)
    
    return hex

num1 = input("Enter a binary number : ")    
print(bin2Dec(num1))
num2 = input("Enter a octal number : ")
print(oct2Hex(num2))

3A
sentence = input("Enter a sentence : ")
wordList = sentence.split(" ")
print("This sentence has", len(wordList), "words")
digCnt = upCnt = loCnt = 0
for ch in sentence:
    if '0' <= ch <= '9':
        digCnt += 1
    elif 'A' <= ch <= 'Z':
        upCnt += 1
    elif 'a' <= ch <= 'z':
        loCnt += 1
print("This sentence has", digCnt, "digits", upCnt, "upper case letters", loCnt, "lower case letters")

3B
str1 = input("Enter String 1 \n")
str2 = input("Enter String 2 \n")
if len(str2) < len(str1):
    short = len(str2)
    long = len(str1)
else:
    short = len(str1)
    long = len(str2)
matchCnt = 0
for i in range(short):
    if str1[i] == str2[i]:
        matchCnt += 1
print("Similarity between two said strings:")
print(matchCnt/long)

4A
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

insertion_sort(input_list)

print("Sorted list using Insertion Sort:", input_list)

MERGE SORT
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
        mergeSort(sub_array1)
        mergeSort(sub_array2)

        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

arr = input('Enter the list of numbers: ').split()
arr = [int(x) for x in arr]
mergeSort(arr)
print('Sorted list: ', end='')
print(arr)


4B
def roman2Dec(romStr):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanBack = list(romStr.upper())[::-1] 
    value = 0
    rightVal = roman_dict[romanBack[0]]
    for numeral in romanBack:
        leftVal = roman_dict[numeral]
        if leftVal < rightVal:
            value -= leftVal
        else:
            value += leftVal
        rightVal = leftVal
    return value

romanStr = input("Enter a Roman Number : ")
print(roman2Dec(romanStr))

5A
import re

def isphonenumber(numStr):
    if len(numStr) != 12:
        return False
    for i in range(len(numStr)):
        if i == 3 or i == 7:
            if numStr[i] != "-":
                return False
        else:
            if not numStr[i].isdigit():
                return False
    return True

def chkphonenumber(numStr):
    ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match(numStr):
        return True
    else:
        return False

ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using Regular Expression")
if chkphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

    
5B

import re

phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')

with open('example.txt', 'r') as f:
    for line in f:
        matches = phone_regex.findall(line)
        for match in matches:
            print(match)
        matches = email_regex.findall(line)
        for match in matches:
            print(match)


6a
import os.path
import sys
fname = input("Enter the filename : ")
if not os.path.isfile(fname):
 print("File", fname, "doesn't exists")
 sys.exit(0)
infile = open(fname, "r")
lineList = infile.readlines()
for i in range(20):
 print(i+1, ":", lineList[i])
 word = input("Enter a word : ")
cnt = 0
for line in lineList:
 cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")


6b

import os
import sys
import pathlib
import zipfile
dirName = input("Enter Directory name that you want to backup : ")
if not os.path.isdir(dirName):
 print("Directory", dirName, "doesn't exists")
 sys.exit(0)

curDirectory = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip", mode="w") as archive:
 for file_path in curDirectory.rglob("*"):
 archive.write(file_path, arcname=file_path.relative_to(curDirectory))

if os.path.isfile("myZip.zip"):
 print("Archive", "myZip.zip", "created successfully")
else:
 print("Error in creating zip archive")

 7a 

 import math
class Shape:
 def __init__(self):
 self.area = 0
 self.name = ""

 def showArea(self):
 print("The area of the", self.name, "is", self.area, "units")

class Circle(Shape):
 def __init__(self,radius):
 self.area = 0
 self.name = "Circle"
 self.radius = radius

 def calcArea(self):
 self.area = math.pi * self.radius * self.radius

class Rectangle(Shape):
 def __init__(self,length,breadth):
 self.area = 0
 self.name = "Rectangle"
 self.length = length
 self.breadth = breadth

 def calcArea(self):
 self.area = self.length * self.breadth
class Triangle(Shape):
 def __init__(self,base,height):
 self.area = 0
 self.name = "Triangle"
 self.base = base
 self.height = height

 def calcArea(self):
 self.area = self.base * self.height / 2


c1 = Circle(5)
c1.calcArea()
c1.showArea()
r1 = Rectangle(5, 4)
r1.calcArea()
r1.showArea()
t1 = Triangle(3, 4)
t1.calcArea()
t1.showArea()

7b

class Employee:
 def __init__(self):
 self.name = ""
 self.empId = ""
 self.dept = ""
 self.salary = 0

 def getEmpDetails(self):
 self.name = input("Enter Employee name : ")
 self.empId = input("Enter Employee ID : ")
 self.dept = input("Enter Employee Dept : ")
 self.salary = int(input("Enter Employee Salary : "))

 def showEmpDetails(self):
 print("Employee Details")
 print("Name : ", self.name)
 print("ID : ", self.empId)
 print("Dept : ", self.dept)
 print("Salary : ", self.salary)

 def updtSalary(self):
 self.salary = int(input("Enter new Salary : "))
 print("Updated Salary", self.salary)

e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()

8

class PaliStr:
 def __init__(self):
 self.isPali = False

 def chkPalindrome(self, myStr):
 if myStr == myStr[::-1]:
 self.isPali = True
 else:
 self.isPali = False

 return self.isPali

class PaliInt(PaliStr):
 def __init__(self):
 self.isPali = False

 def chkPalindrome(self, val):
 temp = val
 rev = 0
 while temp != 0:
 dig = temp % 10
 rev = (rev*10) + dig
 temp = temp //10

 if val == rev:
 self.isPali = True
 else:
 self.isPali = False

 return self.isPali
st = input("Enter a string : ")
stObj = PaliStr()
if stObj.chkPalindrome(st):
 print("Given string is a Palindrome")
else:
 print("Given string is not a Palindrome")
val = int(input("Enter a integer : ")) 
intObj = PaliInt()
if intObj.chkPalindrome(val):
 print("Given integer is a Palindrome")
else:
 print("Given integer is not a Palindrome")

PART B:

AREA OF TRIANGLE:
height = int(input("Enter the height:"))
base = int(input("enter the base:"))
area = 1/2 * base * height
print("the area of triangle:",area)

AREA OF CIRCLE:
import math

radius = int(input("enter the radius:"))
area = math.pi * radius * radius
print("area of circle:",area)



