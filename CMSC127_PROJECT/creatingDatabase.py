import mysql.connector


db =  mysql.connector.connect(
  host  = "localhost",
  user= "root",
  password="kirigiri07",
  database = "finalproject"
)

mycursor = db.cursor()

# CREAETES DATABSE
# mycursor.execute("CREATE DATABASE finalproject")

# CREATES FOOD_ESTABLISHMENT TABLE
# mycursor.execute("""
# CREATE TABLE FOOD_ESTABLISHMENT (
#     Business_id INT(5) PRIMARY KEY ,
#     Name VARCHAR(50) NOT NULL,
#     Address VARCHAR(50) NOT NULL
# )
# """)

# CREATES FOODITEM TABLE
# mycursor.execute("""
#     CREATE OR REPLACE TABLE FOOD_ITEM (
#         Food_id INT(5) PRIMARY KEY,
#         Name VARCHAR(20) NOT NULL,
#         Price NUMERIC(4,2) NOT NULL,
#         Type_of_food VARCHAR(20),
#         Description VARCHAR(50),
#         Business_id INT(5),
#         CONSTRAINT FOOD_ITEM_Business_id_fk FOREIGN KEY(Business_id) REFERENCES FOOD_ESTABLISHMENT(Business_id) on delete cascade
#     )
# """)

# CREATES REVIEW TABLE
# mycursor.execute("""
# CREATE TABLE REVIEW (
#    Review_no INT(5) PRIMARY KEY , 
#     Description VARCHAR(50),
#     Rating decimal(3,2),
#     Time TIME,
#     Date DATE,
#     Business_id INT(5),   
#     Food_id INT(5),
#     CONSTRAINT REVIEW_Business_id_fk FOREIGN KEY(Business_id) REFERENCES FOOD_ESTABLISHMENT(Business_id) on delete cascade,
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
# );
# """)

# mycursor.execute("DROP TABLE IF EXISTS `USER`")
# mycursor.execute("""CREATE TABLE USER (
#     User_id INT(10) PRIMARY KEY,
#     Name VARCHAR(50) NOT NULL,
#     Age INT(2),
#     Password VARCHAR(50) NOT NULL,
#     Username VARCHAR(50) NOT NULL
# )""")


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

# CREATE ANOTHER TABLE FOR FOOD TYPE
# mycursor.execute("""
#     CREATE TABLE FOOD_TYPE
#        ( Foodtype_id INT(2) PRIMARY KEY,
#         Foodtype_name VARCHAR(50))
# """
# )

# if this doesnt work execute in cmd :> || hardcoded values nalang?
# mycursor.execute("""
#     INSERT INTO FOOD_TYPE(Foodtype_id, Foodtype_name) VALUES(1, "Appetizer"),(2, "Entree/Main Dish"),(3, "Sides"),(4, "Dessert")

# """

# )

# CREATES ESTABLISHMENT REVIEW TABLE
# mycursor.execute("""
# CREATE OR REPLACE TABLE ESTABLISHMENT_REVIEW (
#     Review_no INT(5) PRIMARY KEY , 
#     Description VARCHAR(50),
#     Rating decimal(3,2),
#     Time TIME,
#     Date DATE,
#     Business_id INT(5),   
#     User_id INT(10),
#     CONSTRAINT ESTABLISHMENT_REVIEW_Business_id_fk FOREIGN KEY(Business_id) REFERENCES FOOD_ESTABLISHMENT(Business_id) on delete cascade,
#     CONSTRAINT ESTABLISHMENT_REVIEW_User_id_fk FOREIGN KEY (User_id) REFERENCES USER(User_id)
# );
# """)

#  alter table review change column `Review_no` `Review_num` int(5) AUTO_INCREMENT;

#  alter table food_item change column `Food_id` `Food_id` int(5) AUTO_INCREMENT;


#  alter table food_item change column `Price` `Price` int(5);
# alter table establishmentreview change column `Review_no` `Review_no` int(5) auto_increment;

# mycursor.execute("""
#   alter table establishmentreview change column `Review_no` `Review_no` int(5) auto_increment
# """)
# mycursor.execute("""ALTER TABLE establishmentreview DROP FOREIGN KEY ESTABLISHMENTREVIEW_Business_id_fk""")
# ALTER TABLE establishmentreview DROP FOREIGN KEY ESTABLISHMENTREVIEW_Business_id_fk;

# mycursor.execute("""ALTER TABLE ESTABLISHMENTREVIEW CHANGE COLUMN `Business_id` `Business_id` int(5) NULL""")
# mycursor.execute("""update food_establishment set Food_id = NULL""")
# mycursor.execute("""DELETE FROM FOOD_ITEM WHERE Business_id = 12345""")
# mycursor.execute("""DELETE FROM REVIEW WHERE Food_id = 1""")
# mycursor.execute("""DELETE FROM FOOD_ESTABLISHMENT WHERE Business_id = 12345""")
