// Your task is to make a function that can take any non-negative integer as an argument 
// and return it with its digits in descending order. Essentially, rearrange the digits 
// to create the highest possible number.


console.log(Solution(4563));

function Solution(number){
    var stringNumber = number.toString();
    var mayor = 0;
    var mayorString = '';
    var numbers= [];

    for (let index = 0; index < stringNumber.length; index++) {
        numbers.push(stringNumber.charAt(index))
    }
    numbers.sort();
    numbers.reverse();

    numbers.forEach(element => {
        mayorString += element.toString();
    });

    return parseInt(mayorString);
}

function descendingOrder(n){
    return parseInt(String(n).split('').sort().reverse().join(''))
  }