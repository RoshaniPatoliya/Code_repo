
/*$(document).ready(function(){
        $("#btn1").click(function(){
            $(this).css("color","red")
        });
        $("#btn1").dblclick(function(){
            $(this).css("color","green")
        });
});*/

$(document).ready(function(){
    $("#btn1").click(function(){
        alert($("p#get").text());
    });
    $("#btn2").click(function(){
        alert($("p#get").html());
    });
    $("#btn3").click(function(){
        $("p#set").text("Hello <b> World </b>");
    });
    $("#btn4").click(function(){
        $("p#set").html("Hello <b>Lexicon</b>");
    });
    $("#btn5").click(function(){
        alert($("#val").val());
    });
    $("#btn6").click(function(){
        $("#val").val("Lexicon");
    });
    function displayVals()
    {
        var singleVals = $( "#single").val();
        $("p#test").html("<b>Value:</b> " + singleVals);
    }
    $("select").change(displayVals);
    displayVals();
}); 

/*
$(document).ready(function(){
    $("#btn1").click(function(){
        $(this).removeClass("btn btn-success")
    });
});*/