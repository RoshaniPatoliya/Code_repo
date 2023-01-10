
function vat(arra){
    var sum=0;
    var vat=0;
    var total;
    for(i=0; i<arra.length;i++)
    {
    arra[i]= Number(arra[i]) ; 
    sum = sum + arra[i];
    vat= sum * 0.2;
    total= sum + vat;
    }
    console.log("Sum:" +sum);
    console.log("VAT:"+vat);
    console.log("Total:" +total);
}


//vat(['1.20','2.60','3.50']);
vat(['3.12','5','18','19.24','1953.2262','0.001564','1.1445']) ;

/*
function calculateSumAndVAT(arr) {
    let sum = 0;

    for(let price of arr) {
        sum += Number(price);
    }
	//the dollar sign is just like format
	//its an identifier for variables and functions
    console.log(`sum = ${sum}`);
    console.log(`VAT = ${sum * 0.2}`);
    console.log(`total = ${sum * 1.2}`);
}

*/