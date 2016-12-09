// Add odd integers from -300,000 to 300,000 and console.log the final sum. Is
// there a shortcut?

var odds = 0;
for (var num = -300000; num < 300001; num += 1){
    if(num % 2 != 0){
        odds = num + odds;
    }
}

console.log(odds)
