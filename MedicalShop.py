import pymysql
import os
import sys
from dotenv import load_dotenv

load_dotenv("credentials.env")

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db = os.getenv("DB_NAME")


connection = pymysql.connect(host = host,user = user,password = password,database = db)
print(" Connected to MySQL!")
cursor = connection.cursor();

create_table_query = """
CREATE TABLE IF NOT EXISTS medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    stock INT
)
"""
cursor.execute(create_table_query)
print("'medicines' table is ready.")

connection.commit()

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
            print("\nFinal Medicine Database:")
            cursor.execute("SELECT * FROM medicines")
            rows = cursor.fetchall()
            if rows:
                print(f"{'ID':<5}{'Name':<20}{'Price':<10}{'Stock':<10}")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]:<5}{row[1]:<20}{row[2]:<10}{row[3]:<10}")
            else:
                print("No medicines available.")
            print("\nThank You !!!")
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

    cursor.execute("SELECT * FROM medicines where name = %s",(name,))
    result = cursor.fetchone()
    if result:
        while True:
            ask = input(f" Do you want to add stock as {name} already exists ? Press yes to add stock or no to leave : ").lower().strip()
            if ask == "yes":
                try:
                    stock = int(input(" Enter the stock : "))
                    cursor.execute("UPDATE medicines SET stock = stock + %s WHERE name = %s",(stock,name))
                    connection.commit()
                    print(f" Stock updated for {name}")
                    break
                except ValueError:
                        print(" Enter a number")
            elif ask == "no":
                print(f" Stock not updated for {name} medicine")
                break
            else:
                print(" Enter yes or no")
    else:  
        try:
            price = float(input(" Enter the price : "))
            stock = int(input(" Enter the stock : "))
            cursor.execute("INSERT INTO medicines (name,price,stock) VALUES (%s,%s,%s)",(name,price,stock))
            connection.commit()
            print(f" {name} added succesfully")
        except ValueError:
            print(" Please enter a number")   

def removingMedicine():
    name = input(" Enter the name of the Medicine : ").lower().strip()
    cursor.execute("SELECT * FROM medicines WHERE name = %s",(name,))
    result = cursor.fetchone()

    if result:
        cursor.execute("DELETE FROM medicines WHERE name = %s",(name,))
        connection.commit()
        print(f" {name} removed succesfully")
    else:
        print(f" No medicine name {name}")

def searchingMedicine():
    name = input(" Enter the name of the Medicine : ").lower().strip()
    cursor.execute("SELECT * FROM medicines WHERE name = %s",(name,))
    result = cursor.fetchone()

    if result:
        print(" Medicine Found:")
        print(f" {'ID':<5}{'Name':<20}{'Price':<10}{'Stock':<10}")
        print(" -"*50)
        print(f" {result[0]:<5} {result[1]:<20} {result[2]:<10} {result[3]:<10}")
    else:
        print(f" No medicine named '{name}' was found.")

def addingStock():
    name = input(" Enter the name of the Medicine : ").lower().strip()
    cursor.execute("SELECT * FROM medicines WHERE name = %s",(name,))
    result = cursor.fetchone()
    if result:
        try:
            stock = int(input(" Please enter the stock:"))
            cursor.execute("UPDATE medicines SET stock = stock + %s WHERE name = %s",(stock,name))
            connection.commit()
            print(f"Stock for {name} been updated")
        except ValueError:
            print("Enter a number")
    else:
        print(f"No medicine found with {name}")

def buying():
    final_price = 0
    while True:
        name = input(" Enter the medicine : ").lower().strip()
        cursor.execute("SELECT * FROM medicines WHERE name = %s",(name,))
        result = cursor.fetchone()
        if result:
            price_per_unit = result[2] 
            available_stock = result[3]
            try:
                stock = int(input("Please enter the stock : "))
            except ValueError:
                print("Enter a valid number.")
            if stock>available_stock:
                print(f"Only {available_stock} in stock. Cannot process order.")
                break
            total = price_per_unit * stock
            final_price += total
            cursor.execute("UPDATE medicines SET stock = stock - %s WHERE name = %s", (stock, name))
            connection.commit()

            print(f" {stock} units of '{name}' bought for ₹{total:.2f}")
        else:
            print(f"{name} doesnot exist")
        a = input(" Do you want to add another medicine? (yes/no): ").strip().lower()
        if a == "yes":
            continue
        else:
            print(f"\n💰 The final total price is: ₹{final_price:.2f}")
            break


def autoDelete():
    cursor.execute("DELETE FROM medicines WHERE stock = 0")
    connection.commit()

    print("Medicines with 0 stock are removed")

if __name__ == "__main__":
    main()
