/*function nextday_date(arra){
    var year = Number(arra[0]);
    var month = Number(arra[1]);
    var day = Number(arra[2]);
    var today = new Date(year, month-1, day);
    console.log(today);
    let oneDay = 24 * 60 * 60 * 1000;
    let nextDay = new Date(today.getTime() + oneDay);

    console.log(`$-{nextDay.getFullYear()}-${nextDay.getMonth()+1}-${nextDay.getDate()}`);
    
    
 }

nextday_date(['2016','9','30'])*/


function nextDay(arr) {
    let year = Number(arr[0]);
    let month = Number(arr[1]);
    let day = Number(arr[2]);

    let today = new Date(year, month-1, day);
	//console.log(today);
    let oneDay = 24 * 60 * 60 * 1000;
    let nextDay = new Date(today.getTime() + oneDay);
    //console.log (nextDay);
    console.log(`$-{nextDay.getFullYear()}-${nextDay.getMonth()+1}-${nextDay.getDate()}`);
}
var arr = [2016,09,30];
nextDay(arr);