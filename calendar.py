#In this project, we’ll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:
#View the calendar
#Add an event to the calendar
#Update an existing event
#Delete an existing event

from time import sleep, strftime

user_name="Ionela"
calendar={
}

def welcome():
    print("Welcome to your calendar, " + user_name)
    print("Calendar is opening...")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("The clock is: " + strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do?")

def start_calendar():
    welcome()
    start=True
    while(start):
        user_choice=input("Enter A to add, U to update, V to view, D to delete or X to exit: ")
        user_choice=user_choice.upper()
        if user_choice=='V':
            if len(calendar.keys())<1:
                print("The calendar is empty")
            else:
                print(calendar)
        elif user_choice=="U":
            date=input("What date?")
            update=input("Enter the update:")
            calendar[date]=update
            print("Update successfully")
            print(calendar)
        elif user_choice=="A":
            event=input("Enter event: ")
            date=input("Enter date (MM/DD/YYYY): ")
            if len(date)>10 or int(date[6:])<int(strftime("%Y")):
                print("Invalid date")
                try_again=input("Try Again? Y for Yes, N for No: ")
                if try_again=="Y":
                    continue
                else:
                    start=False
            else:
                calendar[date]=event
                print("Event added successfully")
                print(calendar)
        elif user_choice=="D":
            if len(calendar.keys())<1:
                print("Calendar is empty")
            else:
                event=input("What event")
                for date in calendar.keys():
                    if event==calendar[date]:
                        del calendar[date]
                        print("Event successfully deleted")
                        print(calendar)
                    else:
                        print("Incorrect event")
        elif user_choice=="X":
            start=False
        else:
            print("Invalid command")
            exit()

start_calendar()
