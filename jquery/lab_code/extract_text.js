/*$(document).ready(function(){
    $("button").click(function(){
        $("div").text("first item second item third item");
      });
  }); 


  function ExtractText()
            {
               var item = document.getElementById("item").value;
               document.getElementById("result").innerHTML=  +item.innerHTML;         
               //'first item second item third item';
            }  
            */


            function extractText() {
                let result = [];
                $("#items li")
                    .toArray()
                    .map(e => result.push(e.textContent));
                $("#result").text(result.join(", "));
            }    




 