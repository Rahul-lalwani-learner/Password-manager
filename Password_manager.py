import sys
import mysql.connector as conn
Mycon = conn.connect(user='root',password='1234',host='localhost',database='main')
cursor = Mycon.cursor()
def display(data):
    print("_" * 100)
    print("| %-30s | %-30s | %-30s |" % ("Site Name", "UserName", "PassWords"))
    print("_" * 100)
    count=cursor.rowcount
    for row in data:
        print("| %-30s | %-30s | %-30s |" % (row[0], row[1], row[2]))
    print("_" * 100)
    print("#row : {}".format(count))
    print()
def Show_all():
    cursor.execute("Select * from pass;")
    data=cursor.fetchall()
    display(data)
def Search_pass():
    print()
    print("-"*100)
    print()
    print("\t 1. Search With Site Name\n\t 2. Search With UserName ")
    choice=int(input("Enter Your choice (1,2): "))
    if choice==1:
        site = input("Enter Site Name(As you remember):  ")
        cursor.execute("Select * from pass where Site LIKE '%{}%';".format(site))
        data=cursor.fetchall()
        display(data)
    elif choice==2:
        userName=input("Enter User Name (As you remember): ")
        cursor.execute("Select * from pass where UserName LIKE '%{}%';".format(userName))
        data=cursor.fetchall()
        display(data)
    else:
        print("-"*8,"PLZ Enter Valid choice (1,2)","-"*8)
def Add_pass():
    print()
    print("-" * 100)
    print()
    print("\t 1. Add Single Row\n\t 2. Add multiple Rows\n\t 3. Back")
    Choice=int(input("Enter Your choice (1,2,3): "))
    if Choice==1:
        Site = input("Enter Site Name: ")
        UserName = input("Enter UserName: ")
        Password = input("Enter PassWord : ")
        cursor.execute("INSERT into pass values ('{}','{}','{}');".format(Site, UserName, Password))
        Mycon.commit()
        print("Query OK, 1 row affected (0.01 sec)")
    elif Choice==2:
        loop=True
        print("-"*80)
        while(loop):
            Site = input("Enter Site Name: ")
            UserName = input("Enter UserName: ")
            Password = input("Enter PassWord : ")
            cursor.execute("INSERT into pass values ('{}','{}','{}');".format(Site, UserName, Password))
            Mycon.commit()
            print("Query OK, 1 row affected (0.01 sec)")
            print("-"*40)
            loopSet=input("Do You want to add more values (y/n): ")
            print("-" * 80)
            if loopSet.lower()=='n':
                loop=False
            elif loopSet.lower()=='y':
                loop=True
            else:
                loop=False

    elif Choice==3:
        print("-"*8,"Choice Accepted","-"*8)
    else:
        print("-"*8,"PLZ Enter Valid choice (1,2,3)","-"*8)
def Modify():
    print()
    print("-" * 100)
    print()
    print("\t 1. Change data\n\t 2. Delete password\n\t 3. Back")
    Choice=int(input("Enter Your choice(1,2,3): "))
    if Choice==1:
        print("-"*80)
        print("\t1. Change SiteName\n\t2. Change UserName\n\t3. Change password")
        change=int(input("Enter Your choice(1,2,3): "))
        if change==1:
            Site=input("Enter current Sitename: ")
            UserName=input("Enter current Username: ")
            print("-"*40)
            newsite=input("Enter New Sitename: ")
            cursor.execute("update pass set site ='{}' where site LIKE '%{}%' and username LIKE '%{}%';".format(newsite,Site,UserName))
            Mycon.commit()
            print("Query OK, 1 row affected (0.01 sec)")
        elif change==2:
            Site=input("Enter current Sitename: ")
            UserName=input("Enter current Username: ")
            print("-"*40)
            newuser=input("Enter New UserName: ")
            cursor.execute("update pass set username ='{}' where site LIKE '%{}%' and username LIKE '%{}%';".format(newuser,Site,UserName))
            Mycon.commit()
            print("Query OK, 1 row affected (0.01 sec)")
        elif change==3:
            Site = input("Enter current Sitename: ")
            UserName = input("Enter current Username: ")
            print("-" * 40)
            newpass = input("Enter New Password: ")
            cursor.execute( "update pass set password ='{}' where site LIKE '%{}%' and username LIKE '%{}%';".format(newpass, Site,UserName))
            Mycon.commit()
            print("Query OK, 1 row affected (0.01 sec)")
        else:
            print("-"*8,"PLZ Enter Valid choice (1,2,3)","-"*8)
    elif Choice==2:
        print("-"*80)
        Site=input("Enter SiteName of Row: ")
        UserName=input("Enter UserName of Row: ")
        cursor.execute("Delete from pass where site LIKE '%{}%' and username LIKE '%{}%';".format(Site,UserName));
        Mycon.commit()
        print("Query OK, 1 row affected (0.01 sec)")
    elif Choice==3:
        print("-"*8,"Choice Accepted","-"*8)
    else:
        print("-"*8,"PLZ Enter Valid choice (1,2,3)","-"*8)


def Exit():
    print("_"*100)
    print("Created by : Rahul lalwani")
    print("Thank for Using our system")
    print("_"*100)
    print(exit)
    sys.exit()



if Mycon.is_connected():
    login = input("Type Password to Login : ")# Password is same as mysql password
    if login == "1234":
        while(True):
            print("\t 1. Show all Passwords\n\t 2. Search password\n\t 3. Add new password\n\t 4. Modify Data\n\t 5.Exit  ")
            choice=int(input("Enter your choice(1/2/3/4/5) : "))
            if choice==1:
                Show_all()
            elif choice==2:
                Search_pass()
            elif choice==3:
                Add_pass()
            elif choice==4:
                Modify()
            elif choice==5:
                Exit()
            else:
                print("-"*8,"This is Wrong choice ---- PLZ Enter Choice from (1,2,3,4,5) ","-"*8)

    else:
        print("Incorrect password ")

    Mycon.close()
else:
    print("Not connected")
