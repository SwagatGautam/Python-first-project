#imports the library named "datetime" which returns date and time. 
import datetime
time = datetime.datetime.now()
year = str(time.year)
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
second = str(time.second)

#prints bill for SELL
def bill(fname, lname, phone_number, address, Laptop_Buy_List, ship_cost, user_quantity):
    """Prints the format for the bill. Prints the details of the customer
        prints the details of the laptops the user wants to buy, calculates
        the total amount  and the shipping cost
        1.) Prints the bill in the terminal
        2.) Prints the bill in the text file"""
    
    print("\n")
    print("\t\tShop Bill")
    print("\t  Dhapasi-31, Kathmandu")
    print("\t     Phone: 981221121")
    print("---------------------------------------")
    print("\t  Details of Customer ")
    print("---------------------------------------")
    print("First Name:" + str(fname) + "\t" "LastName:" + str(lname))
    print("Contact: " + str(phone_number) + "\t" "Date: " + day + "-" + month + "-" + year)
    print("Address: " + str(address) + "\t" "Time: " + hour + "-" + minute + "-" + second)
    print("---------------------------------------")
    print("\t\tOverall Bill")
    print("---------------------------------------")
    print("ID | Item | Company | Price | Quantity")
    print("---------------------------------------")
    price_with_shipping_cost = 0
    amount = 0
    #iterating through the laptop buy list chosen by the user
    for each in Laptop_Buy_List:
        print(str(each[0]) + "    " + str(each[1]) + "   " +str(each[2]) + "      " + "$" + str(each[3]) + "       " + str(each[4]))
        amount += int(each[5])
    print("---------------------------------------")
    print("\t\tShipping cost: " + "$" + str(ship_cost))
    price_with_shipping_cost = ship_cost + amount
    print("\t\tTotal Amount:" +  "$" + str(price_with_shipping_cost))
    print("---------------------------------------")

    #printing the bill in text file
    file = open("SELL" + "_" + str(fname) + "_" + str(lname) + "_" + str(hour) + str(minute) + str(second) + ".txt", "w")
    file.write("\n")
    file.write("\t\tShop Bill\n")
    file.write("\t  Dhapasi-31, Kathmandu\n")
    file.write("\t     Phone: 981221121\n")
    file.write("---------------------------------------\n")
    file.write("\t  Details of Customer\n")
    file.write("---------------------------------------\n")
    file.write("First Name:" + str(fname) + "\t" "LastName:" + str(lname) + "\n")
    file.write("Contact: " + str(phone_number) + "\t" "Date: " + day + "-" + month + "-" + year + "\n")
    file.write("Address: " + str(address) + "\t" "Time: " + hour + ":" + minute + ":" + second + "\n")
    file.write("---------------------------------------\n")
    file.write("\t\tOverall Bill\n")
    file.write("---------------------------------------\n")
    file.write("ID | Item | Company | Price | Quantity\n")
    file.write("---------------------------------------\n")

    amount = 0
    for each in Laptop_Buy_List:
        file.write(str(each[0]) + "    " + str(each[1]) + "   " + str(each[2]) + "      " + str(each[3]) + "       " + str(each[4]) + "\n")
        amount += int(each[5])

    file.write("---------------------------------------\n")
    file.write("\t\tShipping Cost: " + "$" + str(ship_cost) + "\n")
    price_with_shipping_cost = ship_cost + amount
    file.write("\t\tTotal Cost:" +  "$" + str(price_with_shipping_cost) + "\n")
    file.write("---------------------------------------")
    return "\n"

#Bill when shop purchases the laptop from the manufacturer
def bill_buy(fname, lname, phone_number, address, Laptop_Buy_List, ship_cost, user_quantity):
    """Prints the format for the bill. Prints the details of the customer
        prints the details of the laptops the user wants to buy, calculates the total amount
        without VAT, with VAT, and the shipping cost
        1.) Prints the bill in the terminal
        2.) Prints the bill in the text file"""
    
    print("\n")
    print("\t\t Purchase Bill")
    print("\t  Kalanki-31, Kathmandu")
    print("\t     Phone: 911931121")
    print("---------------------------------------")
    print("  Details of Shop's Employee ")
    print("---------------------------------------")
    print("First Name:" + str(fname) + "\t" "LastName:" + str(lname))
    print("Contact: " + str(phone_number) + "\t" "Date: " + day + "-" + month + "-" + year)
    print("Address: " + str(address) + "\t" "Time: " + hour + "-" + minute + "-" + second)
    print("---------------------------------------")
    print("\t\tOverall Bill")
    print("---------------------------------------")
    print("ID | Item | Company | Price | Quantity")
    print("---------------------------------------")

    amount_without_vat = 0
    for each in Laptop_Buy_List:
        print(str(each[0]) + "    " + str(each[1]) + "   " +str(each[2]) + "      " + str(each[3]) + "       " + str(each[4]))
        amount_without_vat += int(each[5])
        vat_amount = 0.13 * amount_without_vat
        price_with_vat_and_shipping_cost = amount_without_vat + vat_amount + ship_cost
    print("---------------------------------------")
    print("\t\tAmount without VAT:" + "$" + str(amount_without_vat))
    print("\t\tVAT Amount: " + "$" + str(vat_amount))
    print("\t\tShipping cost: " + "$" + str(ship_cost))
    print("\t\tTotal Amount:" +  "$" + str(price_with_vat_and_shipping_cost))
    print("---------------------------------------")

    #printing the bill in text file
    file = open("PURCHASE" + "_" + str(fname) + "_" + str(lname) + "_" + str(hour) + str(minute) + str(second) + ".txt", "w")
    file.write("\n")
    file.write("\t\tPurchase Bill\n")
    file.write("\t  Kalanki-31, Kathmandu\n")
    file.write("\t     Phone: 911931121\n")
    file.write("---------------------------------------\n")
    file.write("\t  Details of Shop's Employee \n")
    file.write("---------------------------------------\n")
    file.write("First Name:" + str(fname) + "\t" "LastName:" + str(lname) + "\n")
    file.write("Contact: " + str(phone_number) + "\t" "Date: " + day + "-" + month + "-" + year + "\n")
    file.write("Address: " + str(address) + "\t" "Time: " + hour + ":" + minute + ":" + second + "\n")
    file.write("---------------------------------------\n")
    file.write("\t\tOverall Bill\n")
    file.write("---------------------------------------\n")
    file.write("ID | Item | Company | Price | Quantity\n")
    file.write("---------------------------------------\n")
    
    amount_without_vat = 0
    for each in Laptop_Buy_List:
        file.write(str(each[0]) + "    " + str(each[1]) + "   " + str(each[2]) + "      " + str(each[3]) + "       " + str(each[4]) + "\n")
        amount_without_vat += int(each[5])
        vat_amount = 0.13 * amount_without_vat
        price_with_vat_and_shipping_cost = amount_without_vat + vat_amount + ship_cost
    file.write("---------------------------------------\n")
    file.write("\t\tAmount without VAT:" + "$" + str(amount_without_vat) + "\n")
    file.write("\t\tVAT Amount: " + "$" + str(vat_amount) + "\n")
    file.write("\t\tShipping cost: " + "$" + str(ship_cost) + "\n")
    file.write("\t\tTotal Amount:" +  "$" + str(price_with_vat_and_shipping_cost) + "\n")
    file.write("---------------------------------------")
    return "\n"

    
