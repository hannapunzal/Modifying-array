# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
# 3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

def firstOption():
    print("Adding an element to the array")
    userFirst = int(input("What do you want to add to the array?" ))
    array.append(userFirst)
    print(f"This is the updated array: {array}")

def secondOption():
    print("Inserting an element to the array")
    userSecond = int(input("Enter an element to add to the array: "))
    position = int(input("Enter which position (0-9) you want it to be put: "))
    array.insert(position,userSecond)
    print(f"This is the updated array: {array}")

def thirdOption():
    print("Modifying an element of the array")
    userThird = int(input("Enter the position of the element (0-9) that you wish to modify: "))
    newInput = int(input("Enter the new element you want to replace it with: "))
    array [userThird] = newInput
    print(f"This is the updated array: {array}")

def fourthOption():
    print("Deleting an element in the array")
    userFourth = int(input("Enter the number that you'd like to remove from the array: "))
    array.remove(userFourth)
    print(f"This is the updated array: {array}")

def fifthOption():
    print("Arranging array in ascending order")
    array.sort()
    print(f"This is the updated array: {array}")

def sixthOption():
    print("Arranging array in descending order")
    array.sort(reverse=True)
    print(f"This is the updated array: {array}")


array = [1,5,4,3,2,10,7,9,8,6]
print(f"Initial array: {array}")
print("""
        1. -> Add an element
        2. -> Insert an element
        3. -> Modify an element
        4. -> Delete an element
        5. Arrange in ascending order
        6. -> Arrange in descending order
        7. -> Exit the program
        """)
while True:
    userOption = int(input("Choose an option to execute to the array: "))
    if userOption >= 1 and userOption <=6:
        break
    
    else:
        print("Invalid option. Please choose from the menu.")

if userOption ==1:
    firstOption()

elif userOption ==2:
                # option 2
    secondOption()

elif userOption ==3:
                # option 3
    thirdOption()

elif userOption ==4:
    fourthOption()
                
elif userOption ==5:
    fifthOption()
                
elif userOption ==6:
    sixthOption()
                
