// For loops
/*
for(initialization;condition;increment)
{
    let numbers = "";
    for(var i=0; i<5; i++)
    {
        numbers = numbers + i;
    }
    console.log("The number is " + numbers);
}
*/

//Example 2
let arr = [1,2,3,4];
/*for(var i=0; i<4 ; i ++)
{
    console.log("The " + i + " elememt of the array is " + arr[i]);
    for(var j=1; j<=arr.length; j++)
    {
        console.log("The " + j + " elememt is " + arr[j-1]);
    }
}*/

// for in loop
/*let car ={
    name:"BMW",
    color:"red",
    model:"Hybrid",
    year:2015
};
let cardata =" ";
for( let x in car)
{
    cardata = cardata+ x + " ";
    cardata = cardata+ car[x] + " ";
}
console.log(cardata); */


// For of loop ( When you are concerned about the order use for of)
let studentarray = ["xyz","34","computers"];
studentarray[1] = "36"; //change array data
studentarray.push("CSE");// insert data in array
studentarray.pop(); // remove inserted element(LIFO)

let studentdata = " ";
for ( let x of studentarray)
{
    studentdata = studentdata + x + " ";   // studentdata += x;
}
console.log(studentdata);