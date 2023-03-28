drop schema IF EXISTS Csims;
CREATE SCHEMA IF NOT EXISTS Csims;
drop database Csims;
create database Csims;
Use Csims;

create table vetement(
	NameOfClothes VARCHAR(100) Default Null,
  Brand VARCHAR(100) Default Null,
  ID int not null,
  Quantity int Default null,
	Size varchar(10) default null,
  Gender char(10) default null,
  Primary Key (ID)
);

create table employee(
	FirstName VARCHAR(100) Default Null,
  LastName VARCHAR(100) Default Null,
  StaffID int not null,
  Phone Numeric(10,0) Default null,
  Primary Key (StaffID)
);

CREATE TABLE receipt (
  vetement_id INT NOT NULL,
  vetement_name VARCHAR(50) NOT NULL,  
  quantity INT NOT NULL,
  order_date DATETIME,
  total_amount DECIMAL(10,2),
  employee_id INT NOT NULL,
  Foreign Key (vetement_id) References vetement(ID)
  Foreign Key (vetement_name) References vetement(NameOfClothes)
  Foreign Key (employee_id) References employee(StaffID)
);

-- CREATE TABLE OrderItems (
--   order_id INT,
--   vetement_id INT,
--   quantity INT,
--   FOREIGN KEY (order_id) REFERENCES receipt(order_id),
--   FOREIGN KEY (vetement_id) REFERENCES vetement(id),
--   PRIMARY KEY (order_id, product_id)
-- );

Insert into vetement(NameOfClothes,Brand,ID,Quantity,Size,Gender)
Values ("T-Shirt","Tokyo",1,9,"M","Male"),
("Sport Dress","Adidas",3,10,"S","Female"),
("Leather Jacket","Louis Vuitton",2,5,"L","Male");

Insert into employee(FirstName,LastName,StaffID,Phone,Email)
Values ("John","Smith",1,1234567890),
("Jane","Doe",2,1234567890);
