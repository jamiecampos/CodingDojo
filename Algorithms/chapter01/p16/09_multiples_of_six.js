// Print multiples of six up to 60,000 using a WHILE

var num = 0;

while (num < 60001){
    if (num % 6 == 0){
        console.log(num);
    }
    num += 1
}
