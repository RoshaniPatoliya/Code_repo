let headOne = document.querySelector("#one");
let headTwo = document.querySelector("#two");
let headThree= document.querySelector("#three");
headOne.addEventListener('mouseover', function(){
    headOne.textContent = "Mouse currently over";
    headOne.style.color = "red";
});
headOne.addEventListener('mouseout', function(){
    headOne.textContent = "Mouse not on me!";
    headOne.style = "color:red";
});
headTwo.addEventListener("click", function(){
    headTwo.textContent = "Clicked on";
    headTwo.style.color = "blue";
});
headThree.addEventListener("dblclick", function(){
    headThree.textContent = "Double Clicked!";
    headThree.style.color = "red";
})