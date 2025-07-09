# Medical Shop Dashboard 🏥💊

A console-based inventory management system for a medical shop, built using **Python** and **MySQL**.  
Employees can add, remove, update, search, and sell medicines through an interactive menu.

---

## 📌 Features

- ✅ Add new medicines to the database  
- ✅ Update stock for existing medicines  
- ✅ Delete medicines by name  
- ✅ Auto-delete medicines with zero stock  
- ✅ Search medicines by name  
- ✅ Buy medicines and calculate total price  
- ✅ View full inventory on exit  
- ✅ Uses `.env` file for secure DB credentials  

---

## 🛠️ Technologies Used

- Python 3  
- MySQL  
- PyMySQL  
- python-dotenv  

---

## 🔐 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Medical-Shop-dashboard.git
cd Medical-Shop-dashboard
```

### 2. Create a `.env` File

Create a `.env` file in the root directory:

```dotenv
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
```

### 3. Install Required Packages

```bash
pip install pymysql python-dotenv
```

### 4. Run the Program

```bash
python main.py
```

---

## 🧪 Sample Menu

```text
 1: Adding a Medicine 
 2: Removing a Medicine 
 3: Searching a Medicine by name 
 4: Adding Stock 
 5: Buying 
 6: Exit
```

---

## 🧹 AutoDelete Feature

Any medicine with `stock = 0` will be automatically deleted from the database to keep the inventory clean.

---

## 📂 Folder Structure

```
Medical-Shop-dashboard/
│
├── main.py              # Main program file
├── .env                 # Environment variables (excluded from git)
├── README.md            # Project documentation
```

---

## 👨‍💻 Author

**Pavan Sathvik Pendyala**

---

## 📢 License

This project is open-source and free to use for educational and personal purposes.
