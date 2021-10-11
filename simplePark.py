import datetime
from os import system
from colorama import Fore
import random

k = datetime.datetime.now()
a = str(k.date())

system('cls')

print(Fore.GREEN + "\t\t\tPARKING MANAGEMENT SYSTEM\t\t\t")

def main():
    system('cls')
    print(Fore.GREEN + "PARKING MANAGEMENT SYSTEM")
    print(Fore.GREEN + "\n1. Entry\n2. Show\n3. Search\n4. Remove\n5. About")
    option = int(input(Fore.GREEN + "Enter your option : "))
    switchers = {
        1: Entry,
        2: Show,
        3: Search,
        4: Remove,
        5: About
    }
    switchers.get(option)()

def Entry():
    system('cls')
    print(Fore.GREEN + "\t\t\tENTRY\t\t\t")
    print(Fore.GREEN + "1. Car\n2. Bike")
    vehicalType = int(input(Fore.GREEN + "Enter your option : "))
    switchers = {
        1: Car,
        2: Bike,
    }
    switchers.get(vehicalType)()

def Car():
    name = input(Fore.GREEN + "Enter Your Name : \n")
    vehicalNo = input(Fore.GREEN + "Enter Your Car No : \n")
    carModel = input(Fore.GREEN + "Enter Your Car Model : \n")
    token = random.randint(100000, 999999)
    print("Here is your Secret Token : ")
    print(token)
    yes = input(Fore.GREEN + "Do you want to go on with this details (Y/N)")
    if (yes == 'Y' or yes == 'y' or yes == 'yes' or yes == 'Yes'):
        f = open('car.txt', 'a')
        f.write(str(token) + '     ' + name.lower() + '    ' + carModel + '     ' + vehicalNo + '    Booking Time: ' + str(k.hour) + ':' + str(k.minute) + '\r\n')
        print(Fore.GREEN + "Your Parking has been booked Sucessfully!!\n")

def Bike():
    name = input(Fore.GREEN + "Enter Your Name : \n")
    vehicalNo = input(Fore.GREEN + "Enter Your Bike No : \n")
    bikeModel = input(Fore.GREEN + "Enter Your Bike Model : \n")
    token = random.randint(100000, 999999)
    print("Here is your Secret Token : ")
    print(token)
    yes = input(Fore.GREEN + "Do you want to go on with this details (Y/N)")
    if (yes == 'Y' or yes == 'y' or yes == 'yes' or yes == 'Yes'):
        f = open('bike.txt', 'a')
        f.write(str(token) + '     ' + name.lower() + '    ' + bikeModel + '     ' + vehicalNo + '    Booking Time: ' + str(k.hour) + ':' + str(k.minute) + '\r\n')
        print(Fore.GREEN + "Your Parking has been booked Sucessfully!!\n")

def Show():
    system('cls')
    print(Fore.GREEN + "\t\t\tSHOWING DATA\t\t\t")
    print(Fore.GREEN + "1. Car\n2. Bike")
    showData = int(input(Fore.GREEN + "Enter Vehical Data You want to see : "))
    switchers = {
        1: showCar,
        2: showBike,
    }
    switchers.get(showData)()

def showCar():
    system('cls')
    print(Fore.GREEN + "\t\t\tSHOWING CAR DATA\t\t\t")
    with open('car.txt', 'r') as f:
        cardata = f.read()
        print(cardata)
        f.close()

def showBike():
    system('cls')
    print(Fore.GREEN + "\t\t\tSHOWING BIKE DATA\t\t\t")
    with open('bike.txt', 'r') as f:
        bikedata = f.read()
        print(bikedata)
        f.close()

def Search():
    system('cls')
    print(Fore.GREEN + "\t\t\tSEARCH\t\t\t")
    print(Fore.GREEN + "1. Car\n2. Bike")
    searchData = int(input(Fore.GREEN + "Enter in which slot you want to search : "))
    switchers = {
        1: searchCar,
        2: searchBike,
    }
    switchers.get(searchData)()

def searchCar():
    system('cls')
    key = input(Fore.GREEN + "Enter Token : ")
    f = open('car.txt', 'r')
    for line in f:
        line = line.rstrip()
        if line.startswith(key):
            print(Fore.GREEN + line)

def searchBike():
    system('cls')
    key = input(Fore.GREEN + "Enter Token : ")
    f = open('bike.txt', 'r')
    for line in f:
        line = line.rstrip()
        if line.startswith(key):
            print(Fore.GREEN + line)

def Remove():
    system('cls')
    print(Fore.GREEN + "\t\t\tREMOVE\t\t\t")
    print(Fore.GREEN + "1. Car\n2. Bike")
    removeData = int(input(Fore.GREEN + "Enter in which slot you want to remove : "))
    switchers = {
        1: removeCar,
        2: removeBike,
    }
    switchers.get(removeData)()

def removeCar():
    system('cls')
    key = input(Fore.GREEN + "Enter Token : ")
    f = open('car.txt')
    tokenline = f.readlines()
    for line in tokenline:
        line = line.rstrip()
        if line.startswith(key):
            index = tokenline.index(line + "\n")
            tokenline[index] = ""
            myFile = open("car.txt", "w")
            myFiles = "".join(tokenline)
            myFile.write(myFiles)
            myFile.close()

def removeBike():
    system('cls')
    key = input(Fore.GREEN + "Enter Token : ")
    f = open('bike.txt')
    tokenline = f.readlines()
    for line in tokenline:
        line = line.rstrip()
        if line.startswith(key):
            index = tokenline.index(line + "\n")
            tokenline[index] = ""
            myFile = open("bike.txt", "w")
            myFiles = "".join(tokenline)
            myFile.write(myFiles)
            myFile.close()

def About():
    system('cls')
    print(Fore.GREEN + "\tPARKING MANAGEMENT SYSTEM\n\n")
    print(Fore.GREEN + "A smart vehicle parking system not only helps to look for parking but also saves time.\nBuild in Python 3.9 and used Tkinter Module.\nMade By Sachin Lohar\nCopyright All Rights Reserved\n\n")
    enter = input(Fore.GREEN + "Press any number to go Back: ")
    main()
        
main()