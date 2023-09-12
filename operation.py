#importing read
import read

#defining a function that calculates valid id for the laptop and returns the value in boolean
def valid_id(dictionary_, Id):
    
    validId = False
    if(Id<=0 or Id > len(dictionary_)):
        validId = False
    
    else:
        validId = True
    return validId

#defining a function that calculates if the user has entered a valid quantity
def valid_quantity(available_laptop_quantity):
    """This function takes the user quantity
        then validates it with the stock quantity.
        returns user_quantity afterwards"""
    
    quantity_loop = True
    while quantity_loop == True:
        #exception handling
        try:
            user_quantity = int(input("Enter the quantity of laptop: "))
            while user_quantity <= 0 or user_quantity > available_laptop_quantity:
                print("\n")
                print("*********** Dear Admin, the quantity you're looking for is not available. Please re-check and try again! ***********")
                print("\n")
                read.table()
                print("\n")
                user_quantity = int(input("Enter the quantity of laptop: "))
            break 
        #catching the error
        except ValueError:
            print("\n")
            print("*********** Invalid! Accepts only Integers ***********")
            print("\n")
            read.table()
    return user_quantity

#defining a function that validates the valid quantity for purchasing
def valid_quantity_buy():
    """Checks if the valid quantity
    for purchasing is entered by the user"""
    quantity_loop = True
    while quantity_loop == True:
        try:
            user_quantity = int(input("Enter the quantity of laptop: "))
            while user_quantity <= 0:
                print("\n")
                print("*********** Dear Admin, the quantity you're looking for is not available. Please re-check and try again! ***********")
                print("\n")
                read.table()
                print("\n")
                user_quantity = int(input("Enter the quantity of laptop: "))
            break 

        except ValueError:
            print("\n")
            print("*********** Invalid! Accepts only Integers ***********")
            print("\n")
            read.table()
    return user_quantity

#deducts the quantity of the laptop 
def deduct_quantity(Id, user_quantity, available_laptop_quantity):

    final_quantity = available_laptop_quantity - user_quantity
    a = print("\n")
    remaining = read.dictionary_()
    remaining[Id][3] = final_quantity
    stock_after_deduction = open("laptop.txt", "w")

    for each in remaining.values():
        stock_after_deduction.write(str(each[0])+","+str(each[1])+","+str(each[2])+","+str(each[3])+","+str(each[4])+","+str(each[5]))
        stock_after_deduction.write("\n")
    stock_after_deduction.close()
    return a

#deducts the quantity of laptop after purchasing
def deduct_quantity_buy(Id, user_quantity, available_laptop_quantity):

    final_quantity = available_laptop_quantity + user_quantity
    a = print("\n")
    remaining = read.dictionary_()
    remaining[Id][3] = final_quantity
    stock_after_deduction = open("laptop.txt", "w")

    for each in remaining.values():
        stock_after_deduction.write(str(each[0])+","+str(each[1])+","+str(each[2])+","+str(each[3])+","+str(each[4])+","+str(each[5]))
        stock_after_deduction.write("\n")
    stock_after_deduction.close()
    return a
