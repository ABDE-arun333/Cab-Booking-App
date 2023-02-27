from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="arunkumar10778", database="booking")
def Get(mobile):
    res = con.cursor()
    sql = f"SELECT Mobile, Name, DOB, Address, Email, Depature, Destination, Distance, Cost FROM Users AS U LEFT JOIN Travel AS T ON U.Mobile = T.Customer_Id WHERE Mobile = {mobile};"
    res.execute(sql)
    result = res.fetchall()
    return result
def Show(mobile):
    if Get(mobile):
        result = Get(mobile)
        print(tabulate(result, headers=["Customer_Id", "Name", "DOB", "Address", "Email", "Depature", "Destination", "Distance", "Cost"]))
        print('\n')
    else:
        print("User Doesn't Exist")
def Post(mobile, name, dob, address, email):
    res = con.cursor()
    query = f"INSERT INTO Users( Mobile, Name, DOB, Address, Email) VALUES('{mobile}', '{name}', '{dob}', '{address}', '{email}');"
    res.execute(query)
    con.commit()
    print("Inserted Successfully! \n")
def Put(mobile, name, dob, address, email):
    res = con.cursor()
    sql = f"UPDATE Users SET Name = '{name}', DOB = '{dob}', Address = '{address}', Email = '{email}' WHERE Mobile = '{mobile}';"
    res.execute(sql)
    con.commit()
    print("Updated Successfully! \n")
def Delete(mobile):
    res = con.cursor()
    if Get(mobile):
        query = f"DELETE FROM Users WHERE Mobile = '{mobile}';"
        res.execute(query)
        con.commit()
        print("Deleted Successfully! \n")
    else:
        print("User Doesn't Exist")
def Book(mobile, pickup, drop):
    locations = [ 'A', 'B', 'C', 'D', 'E', 'F']
    cost = 0
    distance = 0
    start_loc = locations.index(pickup)
    dest_loc = locations.index(drop)
    for i in range(start_loc, dest_loc):
        if i == start_loc:
            distance += 15
            cost += 100 + ((distance - 5) * 10)
        else:
            distance += 15
            cost += 15 * 10
    res = con.cursor()
    query = f"INSERT INTO Travel(Depature, Destination, Distance, Cost, Customer_Id) VALUES('{pickup}', '{drop}', '{distance}', '{cost}', '{mobile}');"
    res.execute(query)
    con.commit()
    print(f"Total Charges : Rs.{cost}")
    print(f"Total Distance : {distance}Kms \n")
while True:
    print("1.Create Customer Details")
    print("2.Edit Customer Details")
    print("3.View Customer Details")
    print("4.Delete Customer Details")
    print("5.Book Taxi")
    print("6.Exit")
    print("Enter a Following Numbers")
    choice = int(input("Please Enter Your Choice : "))
    if choice == 1:
        mobile = input("Enter the Mobile Number : ")
        if(Get(mobile)):
            print("User already Exist \n")
        else:
            name = input("Enter the Name : ")
            dob = input("Enter the DOB in YYYY-MM-DD : ")
            address = input('Enter the Address : ')
            email = input('Enter the Email : ')
            Post( mobile, name, dob, address, email)    
    elif choice == 2:
        mobile = input("Enter the Mobile Number : ")
        if(Get(mobile)):
            name = input("Enter new Name : ")
            dob = input("Enter new DOB in YYYY-MM-DD : ")
            address = input("Enter new Address : ")
            email = input('Enter new Email : ')
            Put( mobile, name, dob, address, email)
        else:
            print("User Doesn't Exist \n")
    elif choice == 3:
        mobile = input("Enter the Mobile Number : ")
        Show(mobile)
    elif choice == 4:
        mobile = input("Enter the Mobile Number : ")
        Delete(mobile)
    elif choice == 5:
        mobile = input("Enter the Mobile Number : ")
        if(Get(mobile)):
            print("Locations : A, B, C, D, E, F")
            pickup = input("Enter the Pickup Location : ")
            drop = input("Enter the Drop Location : ")
            Book(mobile, pickup, drop)
        else:
            print("User Doesn't Exist")
    elif choice == 6:
        quit()
    else:
        print("Invalid Selection . Please Try Again !")