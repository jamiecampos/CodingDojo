// Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

for (var num = 3; num > -301; num -= 1){
    if (num % 3 == 0){
        if (num != -3 && num != -6){
            console.log(num)
        }else{
            continue
        }
    }
}
