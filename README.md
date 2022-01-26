# Password-manager
This is a basic password manager program using python to fullfill my password management requirement

To use this you have to do certain steps 
1. install and donwload mysql database , mysql.connector and python interpreter
2. after installing do this changes in code by opening in any editor like vscode etc
    a. Mycon = conn.connect(user='root',password='1234',host='localhost',database='main')
    set password of your mysql server and set database
    b.  first open mysql then create database viz main 
            Create database main;
    c. create table in mysql named as pass
            Create table pass
            (
                Site varchar(30),
                UserName varchar(30),
                Password varchar(50)
            );
    d. After this step you are all done Enjoy you password manager
