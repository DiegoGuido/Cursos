

console.log(Solution(10));



function Solution(number) {
    if (number<0) {
        return 0;
    }

    var numbers = [];
    var suma = 0;

    for (let index = 0; index < number; index++) {
        if (index%5==0) {
            if (!numbers.includes(index)) {
                numbers.push(index)
                console.log('Se agrego este número: ' + index);
            }
        }  
        if (index%3==0) {
            if (!numbers.includes(index)) {
                numbers.push(index)
                console.log('Se agrego este número: ' + index);
            }
        }   
    }

    numbers.forEach(element => {
        suma += element;
    });

    return suma;
}


