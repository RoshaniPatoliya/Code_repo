/*function counter(x,y) {
    var count = 0;
  const arra = x.split('');
   //console.log(arra);
   for(i=0; i<arra.length;i++) {
      if (arra[i] == y) {
        count++;
      }
    }
    return count;
  }
  var result= counter('panther','n')
  console.log(result);

  
  function countLetterOcurrencesInAString([string, letter]) {
    let count = 0;

    for(let char of string) {
        if(char == letter) {
            count++;
        }
    }

    console.log(count);
}
console.log()*/

function countVowel(str) { 

  // find the count of vowels
  const count = str.match(/[aeiou]/gi).length;

  // return number of vowels
  return count;
}

 console.log(countVowel('Javascript program'));