import mysql.connector
import datetime


class Connection:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="tiger")
        self.mycursor = self.mydb.cursor()
        print(self.mydb)

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS BLOODBANK;")
        self.mycursor.execute("USE BLOODBANK;")

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS REGISTRATION(REGISTRATION_ID VARCHAR(20) PRIMARY KEY, NAME VARCHAR(20), GENDER VARCHAR(10), DATE_OF_BIRTH DATE , PHONE_NO VARCHAR(12),EMAIL_ADDRESS VARCHAR(30), ADDRESS VARCHAR(50) , GOVERNMENT_ID_TYPE VARCHAR(15) , GOVERNMENT_ID VARCHAR(20)  , DATE_OF_REGISTRATION DATE, BLOOD_GROUP VARCHAR(20));")

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS DONATION(DONATION_ID VARCHAR(20) PRIMARY KEY,REGISTRATION_ID VARCHAR(20),NAME VARCHAR(20),BLOOD_GROUP VARCHAR(20) ,DATE_0F_DONATION DATE , FOREIGN KEY (REGISTRATION_ID) REFERENCES REGISTRATION(REGISTRATION_ID));")

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS USERS(USERNAME VARCHAR(20) , PASSWORD VARCHAR(20));")

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS BLOOD_BANK(A_positive_UNITS INT(4),B_positive_UNITS INT(4),AB_positive_UNITS INT(4),0_positive_UNITS INT(4),A_negative_UNITS INT(4),B_negative_UNITS INT(4),AB_negative_UNITS INT(4),0_negative_UNITS INT(4));")

        self.mycursor.execute("SELECT * FROM BLOOD_BANK;")
        resultSet = self.mycursor.fetchall()        #ResultSet is the List of Tuples

        if(len(resultSet) == 0):
            self.mycursor.execute("INSERT INTO BLOOD_BANK VALUES(0 , 0 , 0 , 0 , 0 , 0 , 0 , 0);")

        self.mydb.commit()
        self.mydb.close() #it Closes the Connection with the database



obj = Connection()