'''
Simple interactive shell for sqlite3 with 
add - remove - list - update functions 
'''
# Importing the modules 
import sqlite3, os, time



class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""
    def __str__(self):
        return self.name
        return self.phone
        return self.address
    # add method()
    # 1) connects to database connection file
    # 2) performs insert method in to the table using while loop
    # 3) at the end  by using conditional if/else statement we can
    # 4) continue or break the while loop and back to the main manu 
    def add(self):
        running = True
        while running:
            os.system("clear")
            print("****** Add new contact ******")
            print()
            self.name = input("Name: ")
            time.sleep(0.10)
            self.phone = input("Phone: ")
            time.sleep(0.10)
            self.address = input("Address: ")
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO contacts\
                                   (Name, Phone, Address) VALUES (?,?,?)""",\
                                   (self.name, self.phone, self.address))
            db.commit()
            add_more = input("Add more? (Y?N): ")
            if add_more == "y".lower():
                continue
            else:
                running = False
                print("exiting to main menu")
                time.sleep(1)
                db.close()
                self.menu()

    # update method()
    # 1) connects to database connection file
    # 2) using input method we choose record to update 
    # 3) performs update mathod on chosen record
    # 4) prompt a message as operation done, and call the menu method
    def update(self):
        print("********** Update **********")
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        time.sleep(0.10)
        name = input("Enter the contact name to update: ")
        phone_update = input("Update phone? (Y?N): ")
        if phone_update == "y".lower():
            phone = input("Enter new number: ")
            cursor.execute('''UPDATE contacts SET Phone = ?  WHERE Name = ?''', (phone, name))
            db.commit()
            time.sleep(0.50)
        else:
            pass
        address_update = input("Update adrress? (Y?N): ")
        if address_update == "y".lower():
            address = input("Enter new address: ")
            cursor.execute('''UPDATE contacts SET Address = ?  WHERE Name = ?''', (address, name))
            db.commit()
            time.sleep(0.50)
        else:
            pass
        print("Record updated")
        time.sleep(0.50)
        self.menu()

    # remove method()
    # 1) connects to database connection file
    # 2) using input method we choose record to remove from table
    # 3) performs delete method to remove chosen record from table
    # 4) prompt the user and call the menu method 
    def remove(self):
        print("********** Delete **********")
        print()
        name = input("Enter the name: ")
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        cursor.execute("DELETE FROM contacts WHERE Name = ?",(name,))
        db.commit()
        print("record removed from database!")
        time.sleep(1)
        self.menu()
        
    # get list method
    # 1) set 2 variables one for count internally, one for display records number
    # 2) connects to connection file to sqlite 3
    # 3) performs Select method to choose name, phone, address records from table
    # 4) using cursor.fetchall() function we can print the result with simple
    # for loop
    # 5) at the end using if/elif statements we can have 2 more aditional operation
    # in list function or just quit to the main menu
    def get_list(self):
        count_2 = 0 
        count = 0 
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        os.system("clear")
        print("********** Contacts *********")
        time.sleep(0.50)
        cursor.execute("SELECT Name, Phone, Address FROM contacts")
        results = cursor.fetchall()
        for row in results:
            time.sleep(0.05)
            count_2 += 1
            count += 1
            print(count_2, row)
            if count == 5:
                input("press a key to continue")
                count = 0
            print()
        print()
        time.sleep(0.50)
        print("End of the records")
        Press_key = input("Press a key to continue")
        time.sleep(0.50)
        option = input("Press  U for update  R for remove   Q for main menu: ")
        if option == "u".lower():
            self.update()
        elif option == "r".lower():
            self.remove()
        elif option == "q".lower():
            self.menu()
    # terminate method
    # simply prints exit the program
    def terminate(self):
        print("Exiting the shell")
        time.sleep(0.50)
        print("...")
        time.sleep(0.50)
        print("..")
        time.sleep(0.50)
        print(".")
        time.sleep(0.50)
        exit()
    # menu method
    # simple menu / option functionality
    # by using if/elif statements and calling the correspondence methods 
    def menu(self):
        os.system("clear")
        time.sleep(0.30)
        print("********** Options *********")
        time.sleep(0.05)
        print("1) Add record")
        time.sleep(0.05)
        print("2) Remove record")
        time.sleep(0.05)
        print("3) list records")
        time.sleep(0.05)
        print("4) Update")
        time.sleep(0.05)
        print("5) Terminate")
        print()
        choice = input("Enter the function number: ")
        if choice == "1":
            self.add()
        elif choice == "2":
            self.remove()
        elif choice == "3":
            self.get_list()
        elif choice == "4":
            self.update()
        elif choice == "5":
            self.terminate()
        else:
            print("Wrong entry try again")
            time.sleep(0.50)
            self.menu()
    # main method
    # using os.path.isfile() method to check if connection file to sqlite3
    # exist or not
    # if doesnt exist creates the connection file and creates Tablets by given format
    # if connection file already exist, system simply connect and calls the main manu 
    def main(self):
        os.system("clear")
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(1)
            print("Connected to database")
            time.sleep(2)
            self.menu()
        else:
            print("Connection file doesnt exist")
            time.sleep(1)
            print("Creating new connection file")
            print("please wait")
            time.sleep(1)
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute(""" CREATE TABLE contacts
                                   (Name TEXT, Phone TEXT, Address TEXT)""")
            print("connection file created!")
            time.sleep(0.50)
            self.menu()

#Create an object of class manager
manager = Manager()
# Call the main function of class manager 
manager.main()






