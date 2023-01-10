// class
class Employee
{
    constructor(id,name)
    {
        this.id = id;
        this.name = name;
    }
    detail()
    {
        document.write(this.id + " " + this.name + "<br>");
    }
}
let e1 = new Employee(101,"xyz");
e1.detail();
var e2 = new Employee(102,"abc");
e2.detail();


class Company 
{
    constructor(cid,cname,loc)
    {
        this.id = cid;
        this.name = cname;
        this.loc = loc;
    }
    info()
    {
        document.write(this.id);
    }
    company_details()
    {
        document.write(this.name);
    }
}
var c1 = new Company(1,"abc","sdf");
c1.info();
c1.company_details();

//static class
class Staticdemo
{
    static display()
    {
        return "This is a static method";
    }
}
document.write(Staticdemo.display());


// encapsulation
class Student
{
    constructor()
    {
        var name;
        var marks;
    }
    getName()
    {
        return this.name;
    }
    setName(name)
    {
        this.name = name;
    }
    getMarks()
    {
        return this.marks;
    }
    setMarks(marks)
    {
        if(marks<0 || marks >100)
        {
            alert("Invalid")
        }
        else
        {
            this.marks = marks;
        }
    }
}
/*var stud = new Student();
stud.setName("abc");
//stud.setMarks(101);
document.writeln("<br>" + stud.getName() + "<br>");*/


// Inheritance
class DateInfo extends Date
{
    constructor()
    {
        super();
    }
}
var dt = new DateInfo();
document.writeln(dt.getDate()); 

class DateInfo extends Student
{
    constructor()
    {
        super();
    }
}
var dt = new DateInfo();
dt.setMarks(20);
document.writeln(dt.getMarks());

// Polymorphism
 class A 
{
    constructor(num)
    {
        this.num = num;
    }
    display1()
    {
        document.write("Hi I am from A" + "<br>");
    }
    /*display1(num)
    {
        document.write("The value of number is" + this.num + "<br>");
    }*/
    var a1 = new A();
    a1.display1();
    //a1.display1(20);

class B 
    {
        display1()
        {
            document.write("I am from class B" + "<br>");
        }
    }
    var b = new B();
    b.display1(); 



// Abstraction
/*class Fruit
{
    constructor()
    {
        if(this.constructor == Fruit)
        {
            throw new Error("Abstract classes cant't be instantiated");
        }
    }
    color()
    {
        throw new Error("Method color must be implemented");
    }
    eat()
    {
        document.write("<br> I am eating");
    }
}
class Apple extends Fruit{
    color()
    {
        document.write("<br> I am red");
    }
}
class Mango extends Fruit{
    color()
    {
        document.write("<br> I am Yellow");
    }
}
var apple = new Apple();
apple.eat();
apple.color();

var mango = new Mango();
mango.eat();
mango.color();

