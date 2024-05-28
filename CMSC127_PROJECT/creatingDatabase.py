import mysql.connector

db =  mysql.connector.connect(
  host  = "localhost",
  user= "root",
  password="angel",
  database = "finalproject"
)


mycursor = db.cursor()

# CREAETES DATABSE
# mycursor.execute("CREATE DATABASE finalproject")


# CREATES FOODITEM TABLE
# mycursor.execute("""
#     CREATE TABLE FOOD_ITEM (
#         Food_id INT(5) PRIMARY KEY,
#         Name VARCHAR(20) NOT NULL,
#         Price DECIMAL(4,2) NOT NULL,
#         Type_of_food VARCHAR(20),
#         Description VARCHAR(50),
#         Business_id INT(5)
#     )
# """)

# CREATES FOOD_ESTABLISHMENT TABLE
# mycursor.execute("""
# CREATE TABLE FOOD_ESTABLISHMENT (
#     Business_id INT(5) PRIMARY KEY ,
#     Name VARCHAR(50) NOT NULL,
#     Address VARCHAR(50) NOT NULL,
#     Food_id INT(5)
# )
# """)



# ADDS CONSTRAINT IN FOOITEM TABLE
# mycursor.execute("""
#     ALTER TABLE FOOD_ITEM 
#     ADD CONSTRAINT FOOD_ITEM_Business_id_fk 
#     FOREIGN KEY (Business_id) 
#     REFERENCES FOOD_ESTABLISHMENT(Business_id)
# """)

# ADDS CONSTRAINT IN FOODESTABLISHMENT TABLE
# mycursor.execute("""
#     ALTER TABLE FOOD_ESTABLISHMENT 
#     ADD CONSTRAINT FOOD_ESTABLISHMENT_Food_id_fk
#     FOREIGN KEY (Food_id) 
#     REFERENCES FOOD_ITEM(Food_id)
# """)


# CREATES REVIEW TABLE
# mycursor.execute("""
# CREATE TABLE REVIEW (
#    Review_no INT(5) PRIMARY KEY , 
#     Description VARCHAR(50),
#     Rating decimal(3,2),
#     Time TIME,
#     Date DATE,
#      Business_id INT(5),   
#     Food_id INT(5),
#     CONSTRAINT REVIEW_Business_id_fk FOREIGN KEY(Business_id) REFERENCES FOOD_ESTABLISHMENT(Business_id),
#     CONSTRAINT REVIEW_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD_ITEM(Food_id)
# );
# """)

# CREATES USER TABLE
# mycursor.execute("""
# CREATE TABLE USER (
#     User_id INT(10) PRIMARY KEY,
#     Name VARCHAR(50) NOT NULL,
#     Age INT(2),
#     Password VARCHAR(50) NOT NULL,
#     Username VARCHAR(50) NOT NULL
# )
# """)

# ADD USER ID FOR FOREIGN KEY IN REVIEW TABLE
# mycursor.execute("""
# ALTER TABLE REVIEW 
# ADD COLUMN User_id INT(10)
# """)


# ADDS CONSTRAINT IN USER TABLE
# mycursor.execute("""
# ALTER TABLE REVIEW 
# ADD CONSTRAINT REVIEW_User_id_fk FOREIGN KEY(User_id) REFERENCES USER(User_id)
# """)


# ADDS CONSTRAINT IN REVIEW TABLE
# mycursor.execute("""
#     ALTER TABLE REVIEW 
#     ADD CONSTRAINT REVIEW_User_id_fk
#     FOREIGN KEY (User_id) 
#     REFERENCES USER(User_id)
# """)

#  CONSTRAINT REVIEW_User_id_fk FOREIGN KEY User_id REFERENCES USER(User_id),