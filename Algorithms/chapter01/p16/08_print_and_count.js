// Print all integer multiples of 5, from 512 to 4096. Aferward, also log how
// many there were.


var multiples = 0;
for (var num = 512; num < 4097; num +=1){
    if(num % 5 == 0){
        console.log(num)
        multiples += 1
    }
}

console.log(multiples)
