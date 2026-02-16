#Homework:

#Slicing Operation on your name:

var_name= input("Enter a string: ")

choice = input("Show indexing? (yes/no): ")

# Indexing show if user says yes

if choice == "yes" or choice =="YES":
    length = len(var_name)

    for i in range(length):
        print("Positive Index:", i, var_name[i], i - length,":Negative Index")

#next operation:        

print("\nNext Operation Starting...")
print("\n")
        


## Using Positive index Slicing :

print("Slicing a string using positve indexing :-")
print()

#1.extract first two element of given string using index:
print("First two element of string:", var_name[0:2])
print()


#2 extract Last two element of string
print("last two element of string :",var_name[len(var_name)-2 : len(var_name)])
print()

#3 extract first three element of string
print("First three element of string :", var_name[0:3])
print()

#4 extract first four element of string
print("First four element of string :", var_name[0:4])
print()

#5 extract third to last element of string 
print("Third to last element of string :", var_name[2:len(var_name)])
print()



## Using Negative index Slicing :

print("Slicing a string using negative index :-")
print()

#1 extract last two element
print("last two element of string :", var_name[-2:])
print()

#2 extract last three element
print("last three element of string :", var_name[-3:])
print()

#3 extract last four element of string
print("Last four element of a string :",var_name[-4:])
print()

#4 extract full string 
print("full string:",var_name[-len(var_name):])
print()

#5 extract Reverse string 
print("Resverse string :",var_name[::-1])
print()

## using nagtive to positive index slicing :

print("Slicing a string using neagtive to positive index :-")
print()

#1 extract First Two element of a string 
print("First two element:",var_name[-len(var_name):2])
print()

#2 extract first three element of a string 
print("First Three element :",var_name[-len(var_name):3])
print()

#3 extract first four element of string 
print("First Four element :",var_name[-len(var_name):4])
print()

#4 extract full string 
print("Full string :", var_name[-len(var_name):len(var_name)])
print()

# 5 extract second last to first element of string 
print("second last element to first element of string :",var_name[-2 : : -1])
print()


#Slicing a String Using Positive To Neagtive Index

print("Slicing a String Using Positive To Negative Index :-")
print()

#1 extract First element to second last element of string 
print("First to Second Last element :",var_name[0:-1])
print()

#2 extract second element to second last element
print( "Second element to second last element:",var_name[1:-1])
print()


# 3 extract full string 
print("Full String :", var_name[:])
print()

#4 extract from middle element to last element of string 
print("middle element to last element of string :",var_name[len(var_name)//2:])
print()

#5 extract last element of string 
print("Last element of string :", var_name[len(var_name)-1:])
print()


#Positive Step Size Slicing

print("Positive Step Size Slicing:-")
print()

#1 Extract Every Second element of string.
print("  skipped string with step 2 :", var_name[::2])
print()

#2 extract from second element with step 2
print("from index 1, with step 2:",var_name[1::2])
print()

#3 extract first half string with step 1 
print("first half string with step 1:",var_name[0:len(var_name)//2:1])
print()

#4 extract first half string with step 2
print("First Half string With step 2 :",var_name[0:len(var_name)//2:2])
print()

#5 Reverse String with step 2
print("Reverse string with Step 2:",var_name[::-2])
print()



print("Program is ended...")