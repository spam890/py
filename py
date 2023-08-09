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
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

if __name__ == "__main__":
    input_list = [12, 11, 13, 5, 6, 7]
    sorted_list = merge_sort(input_list)
    print("Original List:", input_list)
    print("Sorted List:", sorted_list)

4B
def roman2Dec(romStr):
    roman_dict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanBack = list(romStr)[::-1]
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

def isphonenumber_regex(number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, number) is not None

# Test the function
phone_number = "415-555-4242"
if isphonenumber_regex(phone_number):
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")
    
5B
import re

def find_phone_numbers(text):
    phone_pattern = r'\+\d{11}'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

def find_email_addresses(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_addresses = re.findall(email_pattern, text)
    return email_addresses

def main():
    file_path = 'textfile.txt'  # Update this with the path to your text file
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            phone_numbers = find_phone_numbers(content)
            email_addresses = find_email_addresses(content)
            
            print("Phone Numbers found:")
            for number in phone_numbers:
                print(number)
            
            print("\nEmail Addresses found:")
            for email in email_addresses:
                print(email)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()


import re

1

2

3

phone_regex = re.compile(r'\+\d{12}')

email_regex = re.compile(r'[A-Za-z0-9. ]+@[A-Za-z0-9]+\.[A-Za-z]{2,}')

4

15

16

with open('example.txt', 'r') as f:

7

8

9

10

for line in f:

I

# Search for phone numbers in the line

matches = phone_regex.findall(line) for match in matches:

print (match)

11

12

13

14

15

matches email_regex. findall (line)

for match in matches:

print(match)







import re

2

def isphonenumber (numStr);

3

if len(numStr) != 12: return False

4

5

for i in range(len(numStr)): if i=-3 or i==7:

6

7

if numstr[i] != "-";

8

return False

9

else:

10

if numstr[i].isdigit() == False:

11

return False

12

return True

A

23

13

14

15

def chkphonenumber (numStr):

ph_no_pattern= re.compile(r'^\d{3}-\d{3}-\d{4}$") if ph_no_pattern.match(numStr):

return True else:

16

17

18

19

return False

20

21

22

23

24

25

26

ph_num = input("Enter a phone number: ")

print("without using Regular Expression") if isphonenumber (ph_num):

print("Valid phone number")

else:

print("Invalid phone number")

print("Using Regular Expression") if chkphonenumber (ph_num): 27

print("Valid phone number") 29

else:

print("Invalid phone number")
