Create table Towns(
ID int,
name varchar(255)
);

Create table Minions(
ID int,
name varchar(255),
age int
);

Alter table Minions add TownId int;
Alter table Towns add primary key(id);
select * from Minions ;

ALTER TABLE Minions
ADD FOREIGN KEY(TownID) REFERENCES Towns(ID);


Create database Movies;
use Movies ;

Create table Movies(
ID int not null,
Title varchar(255)not null,
DirectorId int,
copyrightyear int,
lenght int,
genreid int,
categoryid int,
Rating decimal(2,1),
Notes int,
primary key(id)
);

ALTER TABLE Movies
ADD FOREIGN KEY(categoryID) REFERENCES categories(ID);


insert into Movies  values(207,'kem 60',103,1785,100,502,4,9.1,6054);
select * from categories ;
select * from genres;
select * from directors;
select * from Movies;

Create database student_enroll;
use student_enroll;

Create table bookdetails(
book_isbn int,
title varchar(255),
publisher varchar(255),
áuthor varchar(255)
);

alter table bookdetails add price decimal(4,2);
alter table enroll add check(grade='o'or grade= 'A+'or grade='A' or grade='B+'or grade='B' or grade='RA');
alter table student drop column address;

Create table branch(
branchcode int not null,
branchname varchar(255),
primary key (branchcode)
);

ALTER TABLE student
ADD constraint fk_dcode FOREIGN KEY(departmentcode) REFERENCES department(dcode);








