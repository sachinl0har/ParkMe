from tkinter import *  
import datetime
import random

k = datetime.datetime.now()
a = str(k.date())

def car():
    car = Tk()
    car.geometry("450x300")
    car.config(background='#000000')
    car.title('CAR PARKING')
    heading = Label(car, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
    heading.grid(columnspan=20, pady=10)
    l1 = Label(car, text='Owner Name: ')
    l1.grid(row=1, column=1)
    l2 = Label(car, text='Car No. : ')
    l2.grid(row=2, column=1)
    l3 = Label(car, text='Car Model: ')
    l3.grid(row=3, column=1)
    name = StringVar()
    cno = StringVar()
    cModel = StringVar()
    token = random.randint(100000, 999999)
    nameentry = Entry(car, textvariable=name)
    nameentry.grid(row=1, column=2)
    cnoentry = Entry(car, textvariable=cno)
    cnoentry.grid(row=2, column=2)
    cModeEntry = Entry(car, textvariable=cModel)
    cModeEntry.grid(row=3, column=2)    

    def carDone():
        n = nameentry.get()
        c = cnoentry.get()
        m = cModeEntry.get()
        t = token

        f = open('car.txt', 'a')
        f.write(str(t) + '   ' + n.lower() + '   ' + c + '   ' + m + '   Booking Time: ' + str(k.hour) + ':' + str(k.minute) + '\r\n')
        l = Label(car, text='Car Parking Sucessfully Booked!\nYour Token: ' + str(t) + ' ', font=10)
        l.grid(row=10, column=2)

    s = Button(car, text='Submit', padx=25, bg='white', command=carDone)
    s.grid(row=8, column=1, pady=10)

def bike():
    bike = Tk()
    bike.geometry("450x300")
    bike.config(background='#000000')
    bike.title('BIKE PARKING')
    heading = Label(bike, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
    heading.grid(columnspan=20, pady=10)
    l1 = Label(bike, text='Owner Name: ')
    l1.grid(row=1, column=1)
    l2 = Label(bike, text='Bike No. : ')
    l2.grid(row=2, column=1)
    l3 = Label(bike, text='Bike Model: ')
    l3.grid(row=3, column=1)
    name = StringVar()
    bno = StringVar()
    bModel = StringVar()
    token = random.randint(100000, 999999)
    nameentry = Entry(bike, textvariable=name)
    nameentry.grid(row=1, column=2)
    bnoentry = Entry(bike, textvariable=bno)
    bnoentry.grid(row=2, column=2)
    bModeEntry = Entry(bike, textvariable=bModel)
    bModeEntry.grid(row=3, column=2)

    def bikeDone():
        n = nameentry.get()
        b = bnoentry.get()
        bm = bModeEntry.get()
        t = token

        f = open('bike.txt', 'a')
        f.write(str(t) + '   ' + n.lower() + '   ' + b + '   ' + bm + '   Booking Time: ' + str(k.hour) + ':' + str(k.minute) + '\r\n')
        l = Label(bike, text='Bike Parking Sucessfully Booked!\nYour Token: ' + str(t) + ' ', font=10)
        l.grid(row=10, column=2)

    s = Button(bike, text='Submit', padx=25, bg='white', command=bikeDone)
    s.grid(row=8, column=1, pady=10)

def show():
    show = Tk()
    show.geometry("450x200")
    show.config(background='#000000')
    show.title('DISPLAY ALL DATA')
    heading = Label(show, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
    heading.grid(columnspan=20, pady=10)
    subtitle = Label(show, text='CHOOSE VEHICAL TYPE: ', bg='#000000', fg='#ffffff', font=('Arial', 15))
    subtitle.grid(columnspan=30, pady=20)

    def carf():
        cf = Tk()
        cf.title('Car Parking Data')
        cf.config(background='#000000')
        heading = Label(cf, text='PARKING MANAGEMENT SYSTEM', bg='black', fg='white', font=('Arial', 20))
        heading.grid(columnspan=20, pady=10)
        f = open('car.txt')
        txt = f.read()
        flable = Label(cf, text=txt)
        flable.grid(row=3, columnspan=4)
        cf.mainloop()

    def bikef():
        bk = Tk()
        bk.title('Bike Parking Data')
        bk.config(background='#000000')
        heading = Label(bk, text='PARKING MANAGEMENT SYSTEM', bg='black', fg='white', font=('Arial', 20))
        heading.grid(columnspan=20, pady=10)
        f = open('bike.txt')
        txt = f.read()
        flable = Label(bk, text=txt)
        flable.grid(row=3, columnspan=4)

    b1 = Button(show, text='Car', command=carf, bg='white')
    b1.grid(row=2, column=8)
    b2 = Button(show, text='Bike', command=bikef, bg='white')
    b2.grid(row=2, column=10)

def search():
    search = Tk()
    search.minsize(450, 250)
    search.maxsize(450, 250)
    search.config(background='#000000')
    search.title('SEARCH')
    heading = Label(search, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
    heading.grid(columnspan=20, pady=10)
    subtitle = Label(search, text='CHOOSE VEHICAL TYPE: ', bg='#000000', fg='#ffffff', font=('Arial', 15))
    subtitle.grid(columnspan=30, pady=20)

    def bikes():
        bikes = Tk()
        bikes.minsize(450, 200)
        bikes.maxsize(450, 200)
        bikes.title('Bikes Search')
        bikes.config(background='#000000')
        heading = Label(bikes, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
        heading.grid(columnspan=20, pady=10)
        l1 = Label(bikes, text='Token: ')
        l1.grid(row=3, column=0, pady=10)
        ttoken = StringVar()

        tokenentry = Entry(bikes, textvariable=ttoken)
        tokenentry.grid(row=3, column=1, pady=10)

        def sdone():
            key = tokenentry.get()
            f = open('bike.txt')
            for line in f:
                line = line.rstrip()
                if line.startswith(key):
                    lab = Label(bikes, text=line)
                    lab.grid(row=6, columnspan=10)

        sd = Button(bikes, text='Submit', command=sdone, padx=10, bg='#ffffff')
        sd.grid(row=4, column=1)

    def cars():
        cars = Tk()
        cars.minsize(450, 200)
        cars.maxsize(450, 200)
        cars.title('Car Search')
        cars.config(background='#000000')
        heading = Label(cars, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
        heading.grid(columnspan=20, pady=10)
        l1 = Label(cars, text='Token: ')
        l1.grid(row=3, column=0, pady=10)
        ttoken = StringVar()

        tokenentry = Entry(cars, textvariable=ttoken)
        tokenentry.grid(row=3, column=1, pady=10)

        def sdone():
            key = tokenentry.get()
            f = open('car.txt')
            for line in f:
                line = line.rstrip()
                if line.startswith(key):
                    lab = Label(cars, text=line)
                    lab.grid(row=6, columnspan=10)

        sd = Button(cars, text='Submit', command=sdone, padx=10, bg='#ffffff')
        sd.grid(row=4, column=1)

    b1 = Button(search, text='Car', command=cars, bg='white')
    b1.grid(row=2, column=8)
    b2 = Button(search, text='Bike', command=bikes, bg='white')
    b2.grid(row=2, column=10)
    search.mainloop()

def remove():
    remove = Tk()
    remove.config(bg='#000000')
    remove.minsize(450, 250)
    remove.maxsize(450, 250)
    remove.title('REMOVE')
    heading = Label(remove, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
    heading.grid(columnspan=20, pady=10)
    l1 = Label(remove, text='Token:')
    l1.grid(row=1, column=0)
    ttoken = StringVar()

    tokenentry = Entry(remove, textvariable=ttoken)
    tokenentry.grid(row=1, column=1)

    def removebike():
        key = tokenentry.get()
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

    def removecar():
        key = tokenentry.get()
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

    def Done():
        l = Label(remove, text='Parking Removed Sucessfully!!', font=10)
        l.grid(row=6, column=1)

    b1 = Button(remove, text='Car', command=removecar, bg='white')
    b1.grid(row=2, column=8)
    b2 = Button(remove, text='Bike', command=removebike, bg='white')
    b2.grid(row=2, column=10)

    s = Button(remove, text='Submit', padx=25, bg='#ffffff', command=Done)
    s.grid(row=5, column=1, pady=10)

    remove.mainloop()

def about():
    about = Tk()
    about.geometry("450x200")
    about.config(background='#000000')
    about.title('PARKING MANAGEMENT SYSTEM')
    heading = Label(about, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
    heading.grid(columnspan=20, pady=10)
    description = Label(about, text='A smart vehicle parking system not only helps to look for parking but also\nsaves time.\nBuild in Python 3.9 and used Tkinter Module.\nMade By Sachin Lohar\nCopyright All Rights Reserved', bg='#000000', fg='#ffffff', font=('Arial', 10))
    description.grid(row=2)

def entry():
    add = Tk()
    add.geometry("450x170")
    add.config(background='#000000')
    add.title('PARKING MANAGEMENT SYSTEM')
    heading = Label(add, text='PARKING MANAGEMENT SYSTEM', bg='#000000', fg='#ffffff', font=('Arial', 20))
    heading.grid(columnspan=20, pady=10)
    subtitle = Label(add, text='CHOOSE VEHICAL TYPE: ', bg='#000000', fg='#ffffff', font=('Arial', 15))
    subtitle.grid(columnspan=30, pady=20)
    b1 = Button(add, text='Car', command=car, bg='white')
    b1.grid(row=2, column=8)
    b2 = Button(add, text='Bike', command=bike, bg='white')
    b2.grid(row=2, column=10)

    add.mainloop()

root = Tk()
root.geometry("450x100")
root.config(background='#000000')
root.title('PARKING MANAGEMENT SYSTEM')
title = Label(root, text='PARKING MANAGEMENT SYSTEM', background='#000000', foreground='#ffffff', font=('Arial', 20))
title.grid(columnspan=20, pady=10)
entryFrame = Frame(root, borderwidth=10)
b1 = Button(root, text='Entry', command=entry, bg='white')
b1.grid(row=1, column=1)
b2 = Button(root, text='Show', command=show, bg='white')
b2.grid(row=1, column=6)
b3 = Button(root, text='Search', command=search, bg='white')
b3.grid(row=1, column=10)
b4 = Button(root, text='Remove', command=remove, bg='white')
b4.grid(row=1, column=14)
b5 = Button(root, text='About', command=about, bg='white')
b5.grid(row=1, column=18)


root.mainloop()