#Imports the datetime library to create date variables and get the current date
from datetime import date

#Imports the csv library to write to the birthday sheet more effectively
import csv

#Creates a new blank birthday sheet
def CreateNewSheet():
    #Opens a new file in write mode
    with open("birthdays.csv", "w", newline="") as file:

        #Creates a file writer to write new data to the birthday sheet
        writer = csv.writer(file)

        #Writes the header of the birthday sheet
        writer.writerow(("Month", "Day", "Name"))

#Sorts the birthday sheet by month in ascending order
#NOTE: Birhtdays are grouped by month but some are out of order
def SortSheetByMonth():

    #Creates an empty variable that will store a list of tuples that store the next birthdays
    file_tuple = None

    #Opens the birthday sheet file
    with open("birthdays.csv") as file:

        #Creates a file reader to read the conents of the birthday sheet
        reader = csv.reader(file)
        
        #Creates an empty list to store all of the birthdays in the birthday sheet
        file_list = []
        
        #For each row in the file
        for row in reader:

            #Append the row to the list of birthdays
            file_list.append([row[0], row[1], row[2]])
        
        #Sort the list of birthdays by the month
        file_list.sort(key=lambda x:x[0], reverse=True)

        #Convert the list of sorted birthdays into a tuple
        file_tuple = tuple(file_list)

    #Open the birthday sheet file
    with open("birthdays.csv", "w", newline="") as file:
        #Creates a file writer to write new data to the birthday sheet
        writer = csv.writer(file)

        #For each row in the file
        for row in file_tuple:

            #Writes the birthday on the row to the birthday sheet
            writer.writerow(row)


#Returns a list of the names of people who's birthday are on the specified day
def BirthdaysOnDate(date):
    #Creates an empty list to store the names of people who's birthdays are today
    birthdays_today = []

    #Opens the birthday sheet file
    with open("birthdays.csv") as file:

        #Creates a file reader to read the conents of the birthday sheet
        reader = csv.reader(file)

        #For each row in the file
        for row in reader:

            #Check if the date of the birthday matches the provided date
            if row[0] == str(date.month) and row[1] == str(date.day):
                
                #Add the name to the list of birthday celebrants
                birthdays_today.append(row[2])
    
    #Returns the list of birthday celebrants
    return birthdays_today

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
        #Creates a file writer to write the sorted list of birthdays to the birthday sheet
        writer = csv.writer(file)
        writer.writerow(birthday)

    #Print to the user that the birthday has been added successfully
    print("Successfully added birthday celebrant.")

    #Sort the birthday sheet to find the right spot for the new birthday in the sheet
    SortSheetByMonth()

#Returns the next birthday coming up
#Takes a date as a parameter that is used as the refernce date to deternim which birthdays follow it
def NextBirthdays(reference_date):

    #Stores the day, month and birthday row of the current next birthday
    next_birthday_day = 31
    next_birthday_month = 12
    next_birthday = []

    #Opens the birthday sheet file
    with open("birthdays.csv") as file:

        #Creates a file reader to read the conents of the birthday sheet
        reader = csv.reader(file)

        #For each row in the file
        for row in reader:

            #If the row is the header of the .csv file, skip the row
            if row[0] == "Month":
                continue

            #If the current next birthday matches the birthday in the row
            if next_birthday_month == int(row[0]) and next_birthday_day == int(row[1]):
                #Append the birthday to the list of current next birthdays
                next_birthday.append(row)
            #Else if the month of the birthday is earlier than the current next birthdays and the month of the birthday is after or on the month of the refernce date
            elif int(row[0]) < next_birthday_month and int(row[0]) >= reference_date.month:

                #Set the birthday as the current next birthday
                next_birthday_month = int(row[0])
                next_birthday_day = int(row[1])
                next_birthday = [row]
            #Else if the birthday month is equal to the month of the current target birthday and the birthday day is earlier than the current next birthday and the birthday day is greater than the day of the refernce date
            elif int(row[0]) == next_birthday_month and int(row[1]) < next_birthday_day and int(row[1]) > reference_date.day:
                
                #Set the birthday as the current next birthday
                next_birthday_month = int(row[0])
                next_birthday_day = int(row[1])
                next_birthday = [row]

        #If the list of current next birthdays is empty and the refence date is set to January 1st of next year
        if next_birthday == [] and reference_date == date(date.today().year + 1, 1, 1):

            #Return an empty list
            return []
        #Else if the list of current next birthdays is empty with a difference refernce date
        elif next_birthday == []:
            
            #Return the next birthday now starting from the begining of the next year at January 1st
            return NextBirthdays(date(date.today().year + 1, 1, 1))

        #Return the list of next birthdays
        return next_birthday