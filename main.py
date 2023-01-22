#Imports part of the datetime library to create date variables and get the current date
from datetime import date
#Imports part of the os library to check if the birthday sheet exists already
from os import path

#Imports a bunch of functions related to reading writning and appending to the birthday sheet
import sheet_handling

#Set the application running to true
running = True

#If a birthday sheet does not exist, create a new blank sheet
if not path.exists("birthdays.csv"):
    sheet_handling.CreateNewSheet()

#Get today's date
date_today = date.today()

#Get a list of all the people who's birthdays are today
birthdays_today = sheet_handling.BirthdaysOnDate(date_today)

#Print the current date in the format weekday, month, day, year
print("Today's Date is:", date_today.strftime("%A %B %d %Y"))

#Gets the next birthday
next_birthdays = sheet_handling.NextBirthdays(date_today)

#Print all the names of people who's birthdays are today
if len(next_birthdays) == 0:
    print("No birthdays saved")
elif len(birthdays_today) == 0:
    print("No birthdays today.")
elif len(birthdays_today) == 1:
    print("Today's birthday celebrant is", birthdays_today[0] + ".")
else:
    print("Today's birthday celebrants are", ", ".join(birthdays_today) + ".")

#If there is at least 1 birthday
if len(next_birthdays) > 0:

    #Loops through the list of birthdays and prints them in a neat format
    #NOTE: Year is not set correctly if the next birthday is next year
    print("The next birthday coming up is for ", end = "")
    for celebrant in next_birthdays:
        print(celebrant[2] + ", ", end = "")
    print("on", date(date_today.year, int(next_birthdays[0][0]), int(next_birthdays[0][1])).strftime("%B %d"))

#While the program is running
while running:

    #Ask the user for what they would like to do next
    selcetion = input("\nWhat would you like to do?\n0: Exit the program\n1: Add new birthday celebrant\n2: List all birthdays this month\n")

    #Handle the choice the user made
    match selcetion:
        case "0":
            #Set the program to stop running
            running = False
        case "1":
            #Add a new birthday to the birthday sheet
            sheet_handling.AddNewBirthday()
        case "2":
            #Lists the birthdays that are in the current month
            sheet_handling.ListBirthdaysThisMonth()
        case _:
            #Print unknown input
            print("Unknown input, please try again")