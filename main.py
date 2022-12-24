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
    print("Today's birthday celebrants are", ", ".join(birthdays_today), ".")