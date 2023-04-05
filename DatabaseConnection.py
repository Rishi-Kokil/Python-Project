import mysql.connector

class Connection:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger"
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS BLOODBANK;")
    mycursor.execute("USE BLOODBANK;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS REGISTRATION(REGISTRATION_ID VARCHAR(15) PRIMARY KEY, NAME VARCHAR(20), GENDER VARCHAR(10), DATE_OF_BIRTH DATE , PHONE_NO VARCHAR(12),EMAIL_ADDRESS VARCHAR(30), ADDRESS VARCHAR(50) , GOVERNMENT_ID_TYPE VARCHAR(15) , GOVERNMENT_ID VARCHAR(20)  , DATE_OF_REGISTRATION DATE, BLOOD_GROUP VARCHAR(20));")


    mycursor.execute("CREATE TABLE IF NOT EXISTS DONATION(DONATION_ID VARCHAR(20) PRIMARY KEY,REGISTRATION_ID VARCHAR(20),NAME VARCHAR(20), DATE_0F_DONATION DATE , FOREIGN KEY (REGISTRATION_ID) REFERENCES REGISTRATION(REGISTRATION_ID));")

    mycursor.execute("CREATE TABLE IF NOT EXISTS BLOOD_BANK(A_positive_UNITS INT(4),B_positive_UNITS INT(4),AB_positive_UNITS INT(4),0_positive_UNITS INT(4),A_negative_UNITS INT(4),B_negative_UNITS INT(4),AB_negative_UNITS INT(4),0_negative_UNITS INT(4));")

    mycursor.execute("INSERT INTO BLOOD_BANK VALUES(0 , 0 , 0 , 0 , 0 , 0 , 0 , 0);")

    def checkUsernamePassword(self , uname , password):
        flag = False

        Connection.mycursor.execute("SELECT * FROM USERS;")
        for i in Connection.mycursor:
            print(i)
            if(i[0] == uname and i[1] == password):
                flag = True
                return flag
        return flag

    def register_user(self, registration_id , name , phone , address , date_of_registration , bloodgroup):
        sql = "INSERT INTO REGISTRATION VALUES (%s, %s , %s, %s , %s, %s )"
        val = (registration_id , name , phone , address , date_of_registration , bloodgroup)
        Connection.mycursor.execute(sql,val)


    def donateBlood(self , donation_id , registration_id, name , date , blood_group):
        sql = "INSERT INTO DONATION VALUES (%s, %s , %s, %s , %s )"
        val = (donation_id , registration_id, name , date , blood_group)
        Connection.mycursor.execute(sql, val)

        Connection.mycursor.execute("UPDATE TABLE BLOOD_BANK SET %s = %s + 1" , blood_group)


    def countingNoOfRows(self):
        Connection.mycursor.execute("SELECT COUNT(REGISTRATION_ID) FROM REGISTRATION;")

        for value in Connection.mycursor:
            return value[0]

    def __init__(self):
        print(Connection.mydb)



