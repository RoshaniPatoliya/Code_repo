function rectangle_area(arra){
    var w = Number(arra[0]);
    var h = Number(arra[1]);
    var W = Number(arra[2]);
    var H = Number(arra[3]);
    var r1= Math.min(w,W);
    var r2= Math.min(h,H);
    var area= ((w*h)+(W*H))-(r1*r2);
    console.log (area);
}

rectangle_area(['13','2','5','8']);

/*
function figureArea([w, h, W, H]) {
    let fig1Area = Number(w) * Number(h);
    let fig2Area = Number(W) * Number(H);
    let commonArea = Math.min(Number(w), Number(W)) * Math.min(Number(H), Number(h));

    let figureArea = fig1Area + fig2Area - commonArea;
    return figureArea;
}
;*/