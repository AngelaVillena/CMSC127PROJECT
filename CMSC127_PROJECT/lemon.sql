

DROP DATABASE IF EXISTS `finalproject`;

CREATE OR REPLACE USER 'finalproject'@'localhost' IDENTIFIED BY 'angel';


CREATE DATABASE IF NOT EXISTS `finalproject`;
GRANT ALL ON finalproject.* TO 'finalproject'@'localhost';
USE `finalproject`;

DROP TABLE IF EXISTS `user`;
CREATE TABLE user (
    User_id INT(10) PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Age INT(2),
    Password VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Role VARCHAR(50)
 );

INSERT INTO user (Name, Age, Password, Username, Role) VALUES 
('Alice Smith', 28, PASSWORD('alice_password'), 'alice', 'admin'),
('Bob Johnson', 35, PASSWORD('bob_password'), 'bob', 'user'),
('Charlie Brown', 22, PASSWORD('charlie_password'), 'charlie', 'user'),
('Diana Prince', 30, PASSWORD('diana_password'), 'diana', 'moderator'),
('Eve Adams', 26, PASSWORD('eve_password'), 'eve', 'user');


CREATE TABLE food_establishment (
  Business_id INT(5) PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(50) NOT NULL,
  Address VARCHAR(100) NOT NULL
);

CREATE TABLE food_item (
    Food_id INT(5) PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Price NUMERIC(4,2) NOT NULL,
    Type_of_food VARCHAR(20),
    Description VARCHAR(100),
    Business_id INT(5),
    CONSTRAINT FOOD_ITEM_Business_id_fk FOREIGN KEY(Business_id) REFERENCES FOOD_ESTABLISHMENT(Business_id)
);
CREATE TABLE review (
    Review_no INT(5) PRIMARY KEY AUTO_INCREMENT, 
    Description VARCHAR(50),
    Rating int(5),
    Time TIME,
    Date DATE,
    Business_id INT(5),   
    Food_id INT(5),
    User_id INT(5),
    CONSTRAINT REVIEW_User_id_fk FOREIGN KEY(User_id) REFERENCES user(User_id),
    CONSTRAINT REVIEW_Business_id_fk FOREIGN KEY(Business_id) REFERENCES FOOD_ESTABLISHMENT(Business_id),
    CONSTRAINT REVIEW_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD_ITEM(Food_id)
);

CREATE TABLE establishment_review (
     Review_no INT(5) PRIMARY KEY AUTO_INCREMENT, 
     Description VARCHAR(50),
     Rating int(5),
     Time TIME,
     Date DATE,
     Business_id INT(5),   
     User_id INT(10),
     CONSTRAINT ESTABLISHMENT_REVIEW_Business_id_fk FOREIGN KEY(Business_id) REFERENCES FOOD_ESTABLISHMENT(Business_id) on delete cascade,
     CONSTRAINT ESTABLISHMENT_REVIEW_User_id_fk FOREIGN KEY (User_id) REFERENCES USER(User_id)
 );
INSERT INTO FOOD_ESTABLISHMENT (Name, Address) VALUES 
('Joe\'s Diner', '123 Main St, '),
('Pasta Palace', '456 Elm St,'),
('Burger Barn', '789 Oak St,');

INSERT INTO food_item (Name, Price, Type_of_food, Description, Business_id) VALUES
('Cheeseburger', 8.99, 'Fast Food', 'A delicious cheeseburger with all the fixings', 3),
('Spaghetti', 12.50, 'Italian', 'Classic spaghetti with marinara sauce', 2),
('Pancakes', 5.99, 'Breakfast', 'Fluffy pancakes with syrup', 1);


INSERT INTO REVIEW (Review_no, Description, Rating, Time, Date, Business_id, Food_id, User_id) VALUES
(1, 'Great cheeseburger!', 5, '12:30:00', '2024-05-15', 3, 1, 1),
(2, 'Delicious pancakes', 4, '09:00:00', '2024-05-16', 1, 3, 2),
(3, 'Spaghetti was okay', 3, '18:45:00', '2024-05-17', 2, 2, 3);








