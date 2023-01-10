/*class Circle
{
    constructor(radius)
    {
        var diameter;
        this.radius=radius;
        
    }
    setDiameter(diameter){
       this.diameter = diameter;
       this.radius= 0.5*this.diameter;
       
    }
    getDiameter(){

        this.diameter= 2*this.radius; 
     }
    
    calcArea()
    {
        console.log(this.radius);
        console.log(this.diameter);
        return 3.14*this.radius*this.radius;
    }
}
let c = new Circle(2);
c.setDiameter(4);
c.setDiameter(1.6);
console.log(c.calcArea());*/


class Circle{
    constructor(radius){
        this.radius = radius;
    }

    get diameter(){
        return this.radius * 2;
    }
    set diameter(diameter){
        this.radius = diameter / 2;
    }

    get area(){
        return Math.pow(this.radius, 2) * Math.PI;
    }
}

let c = new Circle(2);
console.log(c.radius);
console.log(c.diameter);
console.log(c.area);
c.diameter=1.6;
console.log(c.radius);
console.log(c.diameter);
console.log(c.area);





