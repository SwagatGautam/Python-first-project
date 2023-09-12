#prints the format for showing the stock table to the user
def table():
    print("The table given below is the details of laptop: ")
    print("==================================================================================================================")
    print("ID\t|\tModel\t|\tBrand\t|\tPrice\t|\tQuantity   |\tProcessor\t|\tGPU")
    print("==================================================================================================================")
    
    laptop_table = open("laptop.txt", "r")
    Id = 1 
    for line in laptop_table:
        print(Id, "\t\t" + line.replace(",", "\t\t"))
        Id = Id + 1
    laptop_table.close()
    print("==================================================================================================================")
    return Id
    

def main_file():
   
    #design for asking the details from the customer 
    print("-----------------------------------------------------------------")
    print("Please kindly fill up your information for bill generation, User!")
    print("-----------------------------------------------------------------")
    print("\n")
    
    #accessing the stock
    print("===================================================================================================================")
    print("ID\t|\tModel\t|\tBrand\t|\tPrice\t|\tQuantity   |\tProcessor\t|\tGPU")
    print("===================================================================================================================")

    laptop_txt = open("laptop.txt","r")
    Id = 1
        
    for line in laptop_txt:
            
        print(Id,"\t\t"+line.replace(",","\t\t"))
        Id = Id + 1
    print("===================================================================================================================")
    laptop_txt.close()
    return Id


#dictionary that returns the values of the stock and is not printed in the program.
def dictionary_():
    laptop_txt = open("laptop.txt", "r")
    laptop_dictionary = {}
    laptop_id = 1

    for line in laptop_txt:
        line = line.replace("\n", "")
        laptop_dictionary.update({laptop_id: line.split(",")})
        laptop_id += 1
    laptop_txt.close()
    return laptop_dictionary

#returns the available quantity of laptop from the main stock
def quantity_of_laptop(Id):
    stock = open("laptop.txt" , "r")
    laptop_stock_dictionary = {}
    Laptop_Id = 1

    for each in stock:
        each = each.replace("\n", "")
        laptop_stock_dictionary.update({Laptop_Id: each.split(",")})
        Laptop_Id = Laptop_Id + 1
        
    available_laptop_quantity = int(stock[Id][3])
    stock.close()
    return available_laptop_quantity

