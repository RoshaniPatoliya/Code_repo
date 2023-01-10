
Create table salesman(
salesman_id int,
name varchar(50),
city varchar(50),
commisson decimal(4,2));

Create table customer(
customer_id int,
cust_name varchar(50),
city varchar(50),
grade int,
salesman_id int);

Create table orders(
ord_no int,
purch_amt money,
ord_date date,
customer_id int,
salesman_id int);


select s.name,c.cust_name,s.city
from salesman s inner join customer c 
on s.city= c.city;

select o.ord_no,o.purch_amt,c.city
from orders o inner join customer c 
on o.salesman_id= c.salesman_id 
where purch_amt between 500 and 2000;

select c.cust_name,c.city,s.name,s.commisson
from customer c inner join  salesman s
on c.salesman_id= s.salesman_id ;

select c.cust_name,c.city,s.name,s.city,s.commisson
from customer c inner join  salesman s
on c.salesman_id != s.salesman_id 
where s.commisson > 0.12;

select c.customer_id,c.cust_name,c.city,c.grade,s.name,s.city
from customer c inner join  salesman s
on c.salesman_id = s.salesman_id 
where grade < 300
order by c.customer_id;

select c.cust_name,c.city,c.grade,s.name,o.ord_no,o.ord_date,o.purch_amt
from customer c inner join  salesman s 
on c.salesman_id = s.salesman_id 
inner join orders o
on s.salesman_id= o.salesman_id
where o.purch_amt > 2000;

select pro_name,pro_price,com_name 
from item_mast i inner join company_mast c
on i.pro_com=c.com_id;







