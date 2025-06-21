import sys
medicine_info = []
def main():
    while True:
        num = options()
        if num == 1:
            addingMedicine()
        elif num == 2:
            removingMedicine()      
        elif num == 3:
            searchingMedicine() 
        elif num  == 4:
            addingStock()
        elif num == 5:
            buying()
        elif num == 6:
            print("Thank You !!!")
            sys.exit()
        else:
            print(" Enter a number between 1 and 6 only")
        autoDelete()


def options():
    while True:
        try:
            a = int(input(f" 1: Adding a Medicine \n 2: Removing a Medicine \n 3: Searching a Medicine by name \n 4: Adding Stock \n 5: Buying \n 6: Exit\n What is your choice : "))
            return a
        except ValueError:
            print(" Please enter an integer")


def addingMedicine():
    name = input(" Enter the name of the Medicine : ").lower().strip()
    for i in medicine_info:
        if i[0] == name:
            while True:
                ask = input(f" Do you want to add stock as {name} already exists ? Press yes to add stock or no to leave : ").lower().strip()
                if ask == "yes":
                    while True:
                        try:
                            stock = int(input(" Enter the stock : "))
                            break
                        except ValueError:
                            print(" Enter a number")
                    i[2] = i[2] + stock
                    print(f" Stock changed for {name} medicine")
                    print(f" {i}")
                    break
                elif ask == "no":
                    print(f" Stock not changed for {name} medicine")
                    print(f" {i}")
                    break
                else:
                    print(" Enter yes or no")
                    continue
            break
        else:  
            if i == medicine_info[-1]:
                while True:
                    try:
                        price = int(input(" Enter the price : "))
                        stock = int(input(" Enter the stock : "))
                        break
                    except ValueError:
                        print(" Please enter a number")
                med = [name,price,stock]      
                medicine_info.append(med)
                print(f" {name} Medicine added successfully!!!")
                break   
            else:
                continue
    if len(medicine_info) == 0:
        while True:
            try:
                price = int(input(" Enter the price : "))
                stock = int(input(" Enter the stock : "))
                break
            except ValueError:
                print(" Please enter a number")
        med = [name,price,stock]
        medicine_info.append(med)
        print(f" {name} Medicine added successfully!!!")   
    print(f" {medicine_info}")

    
def removingMedicine():
    if len(medicine_info)==0:
            print(f" Medicines is empty!!!")
    else:
        name = input(" Enter the name of the Medicine : ").lower().strip()
        for i in medicine_info:
            if i[0] == name:
                medicine_info.remove(i)
                print(f" {name} Medicine removed successfully!!!")
                break
            else:
                if i == medicine_info[-1]:
                    print(f" No medicine with {name} name was found")
                else:
                    continue
        print(f" {medicine_info}")
        
            
def searchingMedicine():
    if len(medicine_info)==0:
            print(f" Medicines is empty!!!")
    else:
        name = input(" Enter the name of the Medicine : ").lower().strip()
        for i in medicine_info:
            if i[0] == name:
                print(f" Name : {i[0]} \n Price : {i[1]} \n Stock : {i[2]}")
                break
            else:
                if i == medicine_info[-1]:
                    print(f" No medicine with {name} name was found")
                else:
                    continue


def addingStock():
    if len(medicine_info)==0:
            print(f" Medicines is empty!!!")
    else:
        name = input(" Enter the name of the Medicine : ").lower().strip()
        while True:
            try:
                stock = int(input(" Enter the stock you want to add : "))
                break
            except ValueError:
                print(" Please enter a number")
        for i in medicine_info:
            if i[0] == name:
                i[2] = i[2]+stock
                print(f" {name} stock updated succesfully!!!")
                print(f" {i}")
            else:
                if i == medicine_info[-1]:
                    print(f" No medicine with {name} name was found")
                else:
                    continue
        print(f" {medicine_info}")
        

def buying():
    if len(medicine_info)==0:
                print(f" Medicines is empty!!!")
    else:
        price  = 0
        while True:
            while True:
                try:
                    name = input(" Enter the medicine : ").lower().strip()
                    stock = int(input(" Enter the number of medicines : "))
                    break
                except ValueError:
                    print(" Enter a number")
            for i in medicine_info:
                curr_price = 0
                if i[0] == name:
                    curr_price = i[1]*stock
                    price = price + (curr_price)
                    i[2] = i[2] - stock
                    print(f" Price : {curr_price}")
                    break
                else:
                    if i == medicine_info[-1]:
                        print(f" No medicine with {name} name was found")
                    else:
                        continue
            while True:
                a = input(" Do you want to add more medicines? To add enter yes or to get final price enter no : ").strip().lower()
                if a == "yes":
                    break
                elif a == "no":
                    print(f" Total Price : {price}")
                    print(" Please Collect the amount from the Customer")
                    break
                else:
                    print(" Enter yes or no")
                    continue
            if a == "yes":
                continue
            else:
                break
        print(f" {medicine_info}")


def autoDelete():
    for i in medicine_info:
        if i[2] == 0:
            medicine_info.remove(i)
            print(f" {i} medicine is removed as it reached to 0 stock")
    print(f" {medicine_info}")
    

if __name__ == "__main__":
    main()