// Print integers from 0 to 255, and with each integer, print the sum so far.

var total = 0

for(i = 0; i < 256; i++){
    total = total + i
    console.log(i + ", " + total)
}
