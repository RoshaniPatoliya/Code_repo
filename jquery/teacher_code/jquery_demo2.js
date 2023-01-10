$(document).ready(function(){
    $("li").parentsUntil("div.ancestors").css({"color":"green","border": "dotted 2px blue"});
    /*$("#btn1").click(function(){
        $("p").append("<b> Added text </b>");
    });*/
});