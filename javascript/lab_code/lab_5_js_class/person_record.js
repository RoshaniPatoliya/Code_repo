/*class Person
{
    constructor(firstName,lastName,age,email)
    {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.email= email;
    }
    toString()
    {    
        
        return  this.firstName + " " + this.lastName + "(Age:" +this.age + " " +"Email:"+this.email +")"; 
         
        
 }
}
let person = new Person('Maria','Petersoon',22,'mp@gmail.com');
console.log (person.toString());*/


class Person{
    constructor(firstName, lastName, age, email){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.email = email;
    }

    toString(){
        return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`;
    }
}

let person = new Person('Maria', 'Petterson', 22, 'mp@gmail.com');

console.log(person.toString());

