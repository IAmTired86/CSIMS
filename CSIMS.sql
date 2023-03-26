drop schema IF EXISTS Csims;
CREATE SCHEMA IF NOT EXISTS Csims;
drop database Csims;
create database Csims;
Use Csims;

create table vetement(
	NameOfClothes VARCHAR(100) Default Null,
    Brand VARCHAR(100) Default Null,
    ID int not null,
    quantity int Default null,
	size varchar(10) default null,
    gender char(10) default null,
    Primary Key (ID)
);

create table employee(
	FirstName VARCHAR(100) Default Null,
    LastName VARCHAR(100) Default Null,
    StaffID Numeric(10,0) not null,
    Phone Numeric(10,0) Default null,
    Email VARCHAR(100) Default Null
);

CREATE TABLE receipt (
  order_id INT AUTO_INCREMENT NOT NULL,
  order_date DATETIME,
  total_amount DECIMAL(10,2),
  payment_method VARCHAR(50)
);

CREATE TABLE Order_Items (
  order_id INT,
  vetement_id INT,
  quantity INT,
  FOREIGN KEY (order_id) REFERENCES receipt(order_id),
  FOREIGN KEY (vetement_id) REFERENCES vetement(id),
  PRIMARY KEY (order_id, product_id)
);

