use RoshniDB;
CREATE TABLE SoftDrink (
  Drinkcode INTEGER PRIMARY KEY,
  Dname VARCHAR(30) NOT NULL,
  Price Decimal(4,2),
  Calories INTEGER
);
select * from SoftDrink ;
INSERT INTO SoftDrink VALUES (101, 'Lime and Lemon', 20.00, 120);
INSERT INTO SoftDrink VALUES (102, 'Apple Drink', 18.00, 120);
INSERT INTO SoftDrink VALUES (103, 'Nature Nectar', 15.00, 115);
INSERT INTO SoftDrink VALUES (104, 'Green Mango', 15.00, 140);
INSERT INTO SoftDrink VALUES (105, 'Aam Panna', 20.00, 135);
INSERT INTO SoftDrink VALUES (106, 'Mango Juice Bahaar', 12.00, 150);

SELECT Drinkcode, dname, Calories  FROM SoftDrink WHERE calories > 120;
SELECT Drinkcode, dname, calories FROM SoftDrink Order by calories desc;
SELECT dname, price from SoftDrink where price between 12.00 and 18.00;
select price+ (price * 0.1) as 'Increase price', Price from Softdrink;
INSERT INTO SoftDrink VALUES (108, 'Orange juice', 14.00, 120);
Delete from SoftDrink where Drinkcode = 102;
select count(distinct price) as 'count distinct price'from SoftDrink ;
select distinct price from SoftDrink ;
select max(calories)as 'Max Calori' from SoftDrink ;
select dname from SoftDrink where Dname like '%mango%';
