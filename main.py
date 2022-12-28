from datetime import date
import csv
import os.path

#Returns a list of the names of people who's birthday is today
def BirthdaysToday():
    #Creates an empty list to store the names of people who's birthdays are today
    birthdays_today = []

    #Opens the birthday sheet file
    with open("birthdays.csv") as file:
        reader = csv.reader(file)

        #For each row in the file
        for row in reader:

            #Check if the date of the birthday matches the current date
            if row[0] == str(date_today.month) and row[1] == str(date_today.day):
                
                #Add the name to the list of birthday celebrants
                birthdays_today.append(row[2])
    
    #Returns the list of birthday celebrants
    return birthdays_today

#Creates a new blank birthday sheet
def CreateNewSheet():
    #Opens a new file in write mode
    file = open("birthdays.csv", "w", newline="")
    writer = csv.writer(file)

    #Writes the header of the birthday sheet
    writer.writerow(("Month", "Day", "Name"))

    #Close the file
    file.close()

#Adds a new birthday to the birthday sheet
def AddNewBirthday():

    #Asks the user for the birthday celebrant's name and birth month
    celebrant_name = input("Enter the name of the birthday celebrant\n")
    month = input("Enter the month of their birthday\n")

    #If the month is more than 2 characters, treat the month as the word
    if len(month) > 2:

        #Convert the  month to all upper case
        month = month.upper()

        #Convert the word into the corresponding number and exit the function if there is no valid month
        match month:
            case "JANUARY":
                month = 1
            case "FEBRUARY":
                month = 2
            case "MARCH":
                month = 3
            case "APRIL":
                month = 4
            case "MAY":
                month = 5
            case "JUNE":
                month = 6
            case "JULY":
                month = 7
            case "AUGUST":
                month = 8
            case "SEPTEMBER":
                month = 9
            case "OCTOBER":
                month = 10
            case "NOVEMBER":
                month = 11
            case "DECEMBER":
                month = 12
            case _:
                print("Error: Invalid month, expected the name of a month")
                return
    #Else the month is in numerical form
    else:
        #Try to convert the month into an int, this will return an error if a string with a length of 2 is used
        #NOTE: this will return an incroect value if a single character with an ASCI value of 1-12 is used
        try:
            if int(month) <= 0 or int(month) >= 13:
                print("Error: Invalid month, expected a number between 1 and 12")
                return
        except ValueError:
            print("Error: Invalid month, expected a number between 1 and 12")
            return

    #Ask the user for the birthday celebrant's day of birth
    day = input("Enter the day of their birthday\n")

    #Check if the day is a nmuber and exit the program if so
    try:
       day = int(day)
    except ValueError:
        print("Error: Invalid day, expected a number between 1 and 31")
        return
    
    #Exit the function if the day is not a real date
    #NOTE: does not account for certian months not having certain days
    if day <= 0 or day >= 32:
        print("Error: Invalid day, expected a number between 1 and 31")
        return

    #Create a tuple to store the birthday information
    birthday = (month, day, celebrant_name)

    #Write the birthday information to the birthday sheet
    with open("birthdays.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(birthday)

    #Print to the user that the birthday has been added successfully
    print("Successfully added birthday celebrant.")

#Set the application running to true
running = True

#If a birthday sheet does not exist, create a new blank sheet
if not os.path.exists("birthdays.csv"):
    CreateNewSheet()

#Get today's date
date_today = date.today()

#Get a list of all the people who's birthdays are today
birthdays_today = BirthdaysToday()

#Print the current date in the format weekday, month, day, year
print("Today's Date is:", date_today.strftime("%A %B %d %Y"))

#Print all the names of people who's birthdays are today
if len(birthdays_today) == 0:
    print("No birthdays today.")
elif len(birthdays_today) == 1:
    print("Today's birthday celebrant is", birthdays_today[0], ".")
else:
    print("Today's birthday celebrants are", ", ".join(birthdays_today) + ".")

#While the program is running
while running:

    #Ask the user for what they would like to do next
    selcetion = input("\nWhat would you like to do?\n0: Exit the program\n1: Add new birthday celebrant\n")

    #Handle the choice the user made
    match selcetion:
        case "0":
            #Set the program to stop running
            running = False
        case "1":
            #Add a new birthday to the birthday sheet
            AddNewBirthday()
        case _:
            #Print unknown input
            print("Unknown input, please try again")