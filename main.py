#importing different modules 
import read, operation, write

#Designing the format
print("\n")
print("\n")
print("\t\t\t\t\t\t   ---------------------")
print("\t\t\t\t\t\t     Swagat Electronics ")
print("\t\t\t\t\t\t   ---------------------")
print("\n")
print("\t\t\t\t\t  _________________________________________")
print("\t\t\t\t\t   Dhapasi, Kathmandu | Phone no.9111919191")
print("\t\t\t\t\t  -----------------------------------------")
print("\n")

print("\t\t===============================================================================================")
print("\t\t\t Welcome to the System Admin! We hope you have a good time exploring our system!")
print("\t\t===============================================================================================")


# declaring a function "main()"
def main():

    """This function  does multiple things, such as:
    1.) Asks user if he/she's buying from the manufacturer or selling to the customers
    2.) Catches Exceptions for:
        i.) Laptop Id  ii.) quantity
    3.) Writes bill for the buy of items as well as purchase of the items
    4.) Call all the functions written in other modules.
    5.) Prints the landing Interface
    6.) Handles the exceptions and many more"""

    #declaring and initializing a variable to boolean value
    #main loop which controls the flow of the program
    loop = True
    while loop == True:
        # Instructions to be performed if the condition is true
        print("\n")
        print("Hello user, please select one of the options below:")
        print("---------------------------------------------------")
        print("Enter SELL to sell Laptop to the Customer.")
        print("Enter BUY to Purchase from Manufacturer.")
        print("Enter EXIT to quit the System.")
        print("---------------------------------------------------")
        print("\n")

        # validates user input
        while loop == True:
            try:
                #asking user for option
                user_input = input("Enter the option to continue: ")
                print("\n")

                #returns error if user inputs invalid entry
                if user_input not in ('BUY', 'SELL', 'EXIT'):
                    print("*********** Invalid input! Please make sure that you're entering a valid entry ***********")
                    print("\n")
                #if the entry is legit, this breaks the condition and exits for further instructions
                else:
                    break
            #Catches error if the user inputs any value other than Integers
            except ValueError:
                print("\n")
                print("*********** Invalid! Accepts only String ***********")
                print("\n")

        #instructions to ber performed if user is selling the item
        if user_input == 'SELL':
            
            #declaring the empty list for appending the desired laptop's details
            Laptop_Buy_List = []
            dictionary_ = read.dictionary_()

            #try catch block for name of the customer
            fname = input("First Name of the Customer: ")

            #isalpha() checks if the input is a String
            while not fname.isalpha():
                print("\n")
                print("*********** Invalid Name ***********")
                print("\n")
                fname = input("First Name of the Customer: ")
            print("\n")

            #try catch block for name of the customer
            lname = input("Last Name of the Customer: ")

            while not lname.isalpha():
                print("\n")
                print("*********** Invalid Name ***********")
                print("\n")
                lname = input("Last Name of the Customer: ")
            print("\n")

            #try catch block for phone number 
            phone_loop = True
            while phone_loop == True:
                try:
                    phone_number = int(input("Contact of the customer: "))
                    print("\n")
                except ValueError:
                    print("\n")
                    print("*********** Invalid Phone Number. Only accepts Integer values ***********")
                    print("\n")
                    continue
                break

            #try catch block for address of the customer
            address  = input("Address of the Customer: ")
            while not address.isalpha():
                print("\n")
                print("*********** Invalid Address ***********")
                print("\n")
                address  = input("Address of the Customer: ")
            print("\n")

            read.table()

            #declaring a variable to boolean return type
            isBuying = True
            while isBuying == True:
                
                Id_Loop = True
                while Id_Loop == True:

                    # Asking user with the Laptop ID
                    try:
                        print("\n")
                        Id = int(input("Please provide the desired Laptop's ID: "))
                        print("\n")

                        #calling the valid_id() function to check if the Id is valid 
                        if (operation.valid_id(dictionary_, Id) == False):
                            print("*********** Invalid input! Please enter a valid ID. ***********")
                            print("\n")
                            read.table()
                            print("\n")

                        else:
                            Id_Loop = False
                            break
                    
                    #catches the error in case if the user inputs value other than Integers
                    except ValueError:
                        print("\n")
                        print("*********** Invalid! Accepts only Integers ***********")
                        print("\n")
                        read.table()

                #available quantity of laptop after purchasing
                available_laptop_quantity = int(dictionary_[Id][3])

                #user quantity of laptops
                user_quantity = operation.valid_quantity(available_laptop_quantity)

                #calling the function of quantity deduction to update the text file 
                operation.deduct_quantity(Id, user_quantity, available_laptop_quantity)

                #storing the laptop details for bill  
                LaptopId = Id
                LaptopName = dictionary_[Id][0]
                Company = dictionary_[Id][1]
                Price = dictionary_[Id][2].replace("$", "")
                Total_Price = int(Price)*int(user_quantity)
                
                #appending the details in empty list for bill
                Laptop_Buy_List.append([LaptopId, LaptopName, Company, Price, user_quantity, Total_Price])

                #continuing the  loop if the user enters "yes"
                buy_loop = True
                while buy_loop == True:
                        print("\n")
                        buy = input("Are you willing to buy more items? (yes/no) ")
                        print("\n")

                        #Validating as to what the user inputs
                        if buy not in ('yes', 'no'):
                            print("*********** Invalid Entry! ***********")
                            print("\n")
                            
                        #instructions for else
                        else:
                            if(buy == 'yes'):
                                isBuying = True
                                read.table()

                            else:
                                isBuying = False
                            break

            #shipping cost.                            
            shipping = True
            while shipping == True:
                    ship = input("Are you willing to ship your product at your doorstep? (yes/no) ")
                    print("\n")
                    ship_cost = 0
                    #Validating as to what the user inputs
                    if ship not in ('yes', 'no'):
                        print("*********** Invalid Entry! ***********")
                        print("\n")
                            
                    #instructions for else
                    else:
                        if(ship == 'yes'):
                            ship_cost += 55
                            print(write.bill(fname, lname, phone_number, address, Laptop_Buy_List, ship_cost, user_quantity))

                        else:
                            ship_cost = 0
                            print("Your bill has been printed")
                            print(write.bill(fname, lname, phone_number, address, Laptop_Buy_List, ship_cost, user_quantity))
                        break
        
        #instructions if the laptop shop wants to buy the product from the manufacturer
        elif user_input == 'BUY':
            
            #declaring the empty list for appending the desired laptop's details
            Laptop_Buy_List = []
            dictionary_ = read.dictionary_()

            #validating first name of the employee
            fname = input("First Name of the Employee: ")

            while not fname.isalpha():
                print("\n")
                print("*********** Invalid Name ***********")
                print("\n")
                fname = input("First Name of the Employee: ")
            print("\n")

            #validating first name of the employee
            lname = input("Last Name of the Employee: ")

            while not lname.isalpha():
                print("\n")
                print("*********** Invalid Name ***********")
                print("\n")
                lname = input("Last Name of the Employee: ")
            print("\n")

            #try catch block for phone number 
            phone_loop = True
            while phone_loop == True:
                try:
                    phone_number = int(input("Contact of the Shop: "))
                    print("\n")
                except ValueError:
                    print("\n")
                    print("*********** Invalid Phone Number. Only accepts Integer values ***********")
                    print("\n")
                    continue
                break

            #try catch block for address of the shop
            address  = input("Address of the Shop: ")
            while not address.isalpha():
                print("\n")
                print("*********** Invalid Address ***********")
                print("\n")
                address  = input("Address of the Shop: ")
            print("\n")

            read.table()

            #declaring a variable to boolean return type
            isBuying = True
            while isBuying == True:
                
                Id_Loop = True
                while Id_Loop == True:
                    # Asking user with the Laptop ID
                    try:
                        print("\n")
                        Id = int(input("Please provide the desired Laptop's ID: "))
                        print("\n")

                        #calling the valid_id() function to check if the Id is valid 
                        if (operation.valid_id(dictionary_, Id) == False):
                            print("*********** Invalid input! Please enter a valid ID. ***********")
                            print("\n")
                            read.table()
                            print("\n")
                        else:
                            Id_Loop = False
                            break
                    #catches the error in case if the user inputs value other than Integers
                    except ValueError:
                        print("\n")
                        print("*********** Invalid! Accepts only Integers ***********")
                        print("\n")
                        read.table()

                #available quantity of laptop after purchasing
                available_laptop_quantity = int(dictionary_[Id][3])

                #user quantity of laptops
                user_quantity = operation.valid_quantity_buy()

                #calling the function of quantity deduction to update the text file 
                operation.deduct_quantity_buy(Id, user_quantity, available_laptop_quantity)

                #storing the laptop details for bill  
                LaptopId = Id
                LaptopName = dictionary_[Id][0]
                Company = dictionary_[Id][1]
                Price = dictionary_[Id][2].replace("$", "")
                Total_Price = int(Price)*int(user_quantity)

                #appending the details in empty list for bill
                Laptop_Buy_List.append([LaptopId, LaptopName, Company, Price, user_quantity, Total_Price])

                #continuing the  loop if the user enters "yes"
                buy_loop = True
                while buy_loop == True:
                        print("\n")
                        buy = input("Are you willing to buy more items? (yes/no) ")
                        print("\n")

                        #Validating as to what the user inputs
                        if buy not in ('yes', 'no'):
                            print("*********** Invalid Entry! ***********")
                            print("\n")
                            
                        #instructions for else
                        else:
                            if(buy == 'yes'):
                                isBuying = True
                                read.table()

                            else:
                                isBuying = False
                            break

            #validating if the user wants to ship                            
            shipping = True
            while shipping == True:
                    ship = input("Are you willing to ship your product at your doorstep? (yes/no) ")
                    print("\n")
                    ship_cost = 0
                    #Validating as to what the user inputs
                    if ship not in ('yes', 'no'):
                        print("*********** Invalid Entry! ***********")
                        print("\n")
                            
                    #instructions for else
                    else:
                        if(ship == 'yes'):
                            ship_cost = ship_cost + 55
                            print(write.bill_buy(fname, lname, phone_number, address, Laptop_Buy_List, ship_cost, user_quantity))

                        else:
                            print("Your bill has been printed")
                            print(write.bill_buy(fname, lname, phone_number, address, Laptop_Buy_List, ship_cost, user_quantity))
                        break

        #instructions if the user chooses to EXIT the system
        elif user_input == 'EXIT':
            loop = False
            print("Thank you for visiting us. We hope to see you again!")
main()    
